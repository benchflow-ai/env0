"""Main seed generator — creates users, folder tree, files, permissions."""

from __future__ import annotations

import os
import pathlib
import uuid
import random
from datetime import datetime, timedelta, timezone

from mock_gdrive.models import Base, get_engine, get_session_factory, init_db, User, File, Permission, Comment
from mock_gdrive.state.snapshots import take_snapshot
from .hierarchy import FOLDER_TREE, USERS
from .content import FILES, SHORTCUTS, FOLDER, SHORTCUT


_TASKS_DIR = (
    pathlib.Path(os.environ["TASKS_DIR"])
    if "TASKS_DIR" in os.environ
    else pathlib.Path(__file__).resolve().parents[5] / "tasks"
)


# --- Scenario dispatch ---

def _seed_default(db, folder_map, primary_user, user_objects, rng):
    """Default scenario: full 500-file drive."""
    file_count = 0
    for file_def in FILES:
        _create_file(db, file_def, folder_map, primary_user, user_objects, rng)
        file_count += 1
    for sc_def in SHORTCUTS:
        _create_shortcut(db, sc_def, folder_map, primary_user, rng)
        file_count += 1
    filler_count = _generate_filler_files(db, folder_map, primary_user, rng, target_total=500 - file_count)
    return file_count + filler_count


def _load_needles_module(
    task_dir_name: str | None = None,
    task_data_path: str | None = None,
):
    """Load needles.py from legacy tasks/ or explicit task data path."""
    import importlib.util
    import sys

    if task_data_path:
        needles_path = pathlib.Path(task_data_path) / "needles.py"
    else:
        if not task_dir_name:
            raise ValueError("task_dir_name or task_data_path required")
        needles_path = _TASKS_DIR / task_dir_name / "data" / "needles.py"
    if not needles_path.exists():
        raise ValueError(f"No needles.py found at: {needles_path}")

    module_suffix = (
        task_dir_name.replace("-", "_")
        if task_dir_name
        else f"path_{abs(hash(str(needles_path.resolve())))}"
    )
    module_name = f"needles_{module_suffix}"
    spec = importlib.util.spec_from_file_location(module_name, needles_path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = mod
    spec.loader.exec_module(mod)
    return mod


def _seed_task_scenario(
    db,
    folder_map,
    primary_user,
    user_objects,
    rng,
    task_dir_name: str | None = None,
    task_data_path: str | None = None,
):
    """Per-task seed: load needles from legacy tasks/ or explicit task data path."""
    mod = _load_needles_module(task_dir_name=task_dir_name, task_data_path=task_data_path)

    needles = getattr(mod, "NEEDLES", [])
    normal_files = getattr(mod, "NORMAL_FILES", [])
    fill_config = getattr(mod, "FILL_CONFIG", {})
    task_folders = getattr(mod, "TASK_FOLDERS", [])
    comments = getattr(mod, "COMMENTS", [])

    file_count = 0

    for folder_path in task_folders:
        _ensure_folder_path(db, folder_map, folder_path, primary_user, rng)

    # Create needle files (sensitive, overshared)
    for needle in needles:
        file_def = {
            "name": needle["name"],
            "mimeType": needle["mimeType"],
            "folder": needle.get("folder"),
            "content_text": needle.get("content_text"),
            "id": needle.get("id"),
            "days_ago": needle.get("days_ago"),
            "modified_days_ago": needle.get("modified_days_ago"),
            "shared_with": list(needle.get("shared_with", [])),
        }
        overshare = needle.get("overshare", {})
        if overshare:
            file_def["shared_with"].append(overshare)
        _create_file(db, file_def, folder_map, primary_user, user_objects, rng)
        file_count += 1

    # Create normal files
    for nf in normal_files:
        file_def = {
            "name": nf["name"],
            "mimeType": nf["mimeType"],
            "folder": nf.get("folder"),
            "content_text": nf.get("content_text"),
            "id": nf.get("id"),
            "days_ago": nf.get("days_ago"),
            "modified_days_ago": nf.get("modified_days_ago"),
            "shared_with": list(nf.get("shared_with", [])),
        }
        _create_file(db, file_def, folder_map, primary_user, user_objects, rng)
        file_count += 1

    for comment_def in comments:
        _create_comment(db, comment_def, user_objects, rng)

    # Generate filler files to reach target count
    target_count = fill_config.get("target_count", 0)
    if target_count > file_count:
        filler_count = _generate_filler_files(
            db, folder_map, primary_user, rng,
            target_total=target_count - file_count,
        )
        file_count += filler_count

    return file_count


def _make_task_scenario(task_dir_name: str):
    """Create a scenario key for a specific repo task."""
    return f"task:{task_dir_name}"


# Auto-discover task scenarios from root tasks directory
_TASK_SCENARIOS: set[str] = set()
if _TASKS_DIR.is_dir():
    for _task_dir in sorted(_TASKS_DIR.iterdir()):
        if _task_dir.is_dir() and (_task_dir / "data" / "needles.py").exists():
            _TASK_SCENARIOS.add(_task_dir.name)


def seed_database(
    scenario: str = "default",
    seed: int = 42,
    db_path: str | None = None,
    num_users: int | None = None,
    task_data_path: str | None = None,
    task_name: str | None = None,
) -> dict:
    """Seed the database with a realistic Google Drive structure.

    Returns a summary dict with counts.
    """
    engine = init_db(db_path)
    Base.metadata.create_all(engine)

    SessionLocal = get_session_factory()
    db = SessionLocal()
    rng = random.Random(seed)

    # Determine if this is a task scenario
    task_dir_name = None
    if task_data_path:
        task_dir_name = task_name
    elif scenario.startswith("task:"):
        task_dir_name = scenario[5:]
        if task_dir_name not in _TASK_SCENARIOS:
            available = ["default"] + [f"task:{t}" for t in sorted(_TASK_SCENARIOS)]
            raise ValueError(f"Unknown scenario: {scenario!r}. Available: {available}")
    elif scenario != "default":
        available = ["default"] + [f"task:{t}" for t in sorted(_TASK_SCENARIOS)]
        raise ValueError(f"Unknown scenario: {scenario!r}. Available: {available}")

    try:
        # --- Create users ---
        # For task scenarios, add external@example.com if needed
        users_list = list(USERS)
        if task_dir_name or task_data_path:
            # Add external user for task scenarios that need it
            ext_exists = any(u["email"] == "external@example.com" for u in users_list)
            if not ext_exists:
                users_list.append({
                    "id": "user_external",
                    "email": "external@example.com",
                    "display_name": "External Contractor",
                })

        users_to_create = users_list if num_users is None else users_list[:max(1, num_users)]
        user_objects = {}
        for u in users_to_create:
            user = User(
                id=u["id"],
                email=u["email"],
                display_name=u["display_name"],
            )
            db.add(user)
            user_objects[u["email"]] = user
        db.flush()

        primary_user = user_objects.get("alex@nexusai.com") or list(user_objects.values())[0]

        # --- Create folder tree ---
        folder_map: dict[str, str] = {}  # path -> file_id
        _create_folder_tree(db, FOLDER_TREE, None, "", folder_map, primary_user, rng)
        db.flush()

        # --- Scenario dispatch ---
        if task_dir_name or task_data_path:
            file_count = _seed_task_scenario(
                db,
                folder_map,
                primary_user,
                user_objects,
                rng,
                task_dir_name=task_dir_name,
                task_data_path=task_data_path,
            )
        else:
            file_count = _seed_default(db, folder_map, primary_user, user_objects, rng)

        db.commit()

        # Save initial snapshot
        take_snapshot("initial")

        folder_count = len(folder_map)
        perm_count = db.query(Permission).count()

        return {
            "users": len(users_to_create),
            "folders": folder_count,
            "files": file_count,
            "total_items": folder_count + file_count,
            "permissions": perm_count,
            "scenario": task_dir_name or scenario,
        }
    finally:
        db.close()


def _create_folder_tree(
    db, tree: dict, parent_id: str | None, path_prefix: str,
    folder_map: dict, owner: User, rng: random.Random,
):
    """Recursively create folders from the hierarchy definition."""
    for name, children in tree.items():
        folder_id = uuid.uuid4().hex
        path = f"{path_prefix}/{name}".lstrip("/")
        folder_map[path] = folder_id

        days_ago = rng.randint(30, 365)
        created = datetime.now(timezone.utc) - timedelta(days=days_ago)

        folder = File(
            id=folder_id,
            name=name,
            mime_type=FOLDER,
            parent_id=parent_id,
            owner_id=owner.id,
            last_modifying_user_id=owner.id,
            created_time=created,
            modified_time=created + timedelta(days=rng.randint(0, days_ago)),
        )
        db.add(folder)

        # Owner permission
        db.add(Permission(
            id=uuid.uuid4().hex,
            file_id=folder_id,
            role="owner",
            type="user",
            email_address=owner.email,
            display_name=owner.display_name,
        ))

        if children:
            _create_folder_tree(db, children, folder_id, path, folder_map, owner, rng)


def _create_file(
    db, file_def: dict, folder_map: dict, primary_user: User,
    user_objects: dict, rng: random.Random,
):
    """Create a single file from a file definition."""
    file_id = file_def.get("id") or uuid.uuid4().hex
    folder_path = file_def.get("folder")
    parent_id = folder_map.get(folder_path) if folder_path else None

    days_ago = file_def.get("days_ago") or rng.randint(1, 300)
    created = datetime.now(timezone.utc) - timedelta(days=days_ago)
    modified_days_ago = file_def.get("modified_days_ago")
    if modified_days_ago is not None:
        modified = datetime.now(timezone.utc) - timedelta(days=modified_days_ago)
    else:
        modified = created + timedelta(days=rng.randint(0, min(days_ago, 60)))

    owner_email = file_def.get("owner", primary_user.email)
    owner = user_objects.get(owner_email, primary_user)

    content_text = file_def.get("content_text")
    content_blob = file_def.get("content_blob")
    size = len(content_blob) if content_blob else (len(content_text.encode()) if content_text else 0)

    f = File(
        id=file_id,
        name=file_def["name"],
        mime_type=file_def["mimeType"],
        parent_id=parent_id,
        owner_id=owner.id,
        last_modifying_user_id=owner.id,
        created_time=created,
        modified_time=modified,
        content_text=content_text,
        content_blob=content_blob,
        size=size,
        description=file_def.get("description"),
    )
    db.add(f)

    # Owner permission
    db.add(Permission(
        id=uuid.uuid4().hex,
        file_id=file_id,
        role="owner",
        type="user",
        email_address=owner.email,
        display_name=owner.display_name,
    ))

    # Additional sharing
    for share in file_def.get("shared_with", []):
        perm_type = share.get("type", "user")
        db.add(Permission(
            id=uuid.uuid4().hex,
            file_id=file_id,
            role=share["role"],
            type=perm_type,
            email_address=share.get("email"),
            display_name=share.get("display_name"),
            domain=share.get("domain"),
        ))        


def _ensure_folder_path(
    db,
    folder_map: dict,
    folder_path: str,
    owner: User,
    rng: random.Random,
):
    """Create a task-specific folder path if it does not already exist."""
    if not folder_path:
        return

    parent_id = None
    built_path = ""
    for part in folder_path.split("/"):
        built_path = f"{built_path}/{part}".lstrip("/")
        existing_id = folder_map.get(built_path)
        if existing_id:
            parent_id = existing_id
            continue

        days_ago = rng.randint(30, 365)
        created = datetime.now(timezone.utc) - timedelta(days=days_ago)
        folder_id = uuid.uuid4().hex

        db.add(File(
            id=folder_id,
            name=part,
            mime_type=FOLDER,
            parent_id=parent_id,
            owner_id=owner.id,
            last_modifying_user_id=owner.id,
            created_time=created,
            modified_time=created,
        ))
        db.add(Permission(
            id=uuid.uuid4().hex,
            file_id=folder_id,
            role="owner",
            type="user",
            email_address=owner.email,
            display_name=owner.display_name,
        ))
        folder_map[built_path] = folder_id
        parent_id = folder_id


def _create_comment(db, comment_def: dict, user_objects: dict, rng: random.Random):
    """Create a seeded comment attached to a task file."""
    file_id = comment_def["file_id"]
    author_email = comment_def.get("author", "alex@nexusai.com")
    author = user_objects.get(author_email)
    if not author:
        return

    days_ago = comment_def.get("days_ago", rng.randint(1, 30))
    created = datetime.now(timezone.utc) - timedelta(days=days_ago)

    db.add(Comment(
        id=comment_def.get("id", uuid.uuid4().hex),
        file_id=file_id,
        author_id=author.id,
        content=comment_def.get("content", ""),
        html_content=comment_def.get("html_content"),
        created_time=created,
        modified_time=created,
        resolved=comment_def.get("resolved", False),
        deleted=comment_def.get("deleted", False),
        anchor=comment_def.get("anchor"),
        quoted_file_content_value=comment_def.get("quoted_file_content_value"),
        quoted_file_content_mime_type=comment_def.get("quoted_file_content_mime_type"),
    ))


def _create_shortcut(
    db, sc_def: dict, folder_map: dict, owner: User, rng: random.Random,
):
    """Create a shortcut file pointing to another file."""
    file_id = uuid.uuid4().hex
    parent_id = folder_map.get(sc_def["folder"])

    # Find target file by name and folder
    target_folder_id = folder_map.get(sc_def["target_folder"])
    target = db.query(File).filter(
        File.name == sc_def["target_name"],
        File.parent_id == target_folder_id,
    ).first()

    if not target:
        return  # Target not found, skip

    created = datetime.now(timezone.utc) - timedelta(days=rng.randint(1, 180))

    f = File(
        id=file_id,
        name=sc_def["name"],
        mime_type=SHORTCUT,
        parent_id=parent_id,
        owner_id=owner.id,
        last_modifying_user_id=owner.id,
        created_time=created,
        modified_time=created,
        shortcut_target_id=target.id,
        shortcut_target_mime_type=target.mime_type,
    )
    db.add(f)

    db.add(Permission(
        id=uuid.uuid4().hex,
        file_id=file_id,
        role="owner",
        type="user",
        email_address=owner.email,
        display_name=owner.display_name,
    ))


def _generate_filler_files(
    db, folder_map: dict, owner: User, rng: random.Random, target_total: int,
) -> int:
    """Generate additional filler files to reach the target count."""
    if target_total <= 0:
        return 0

    from faker import Faker
    from mock_gdrive.seed.content import DOC, SHEET, PDF, PNG, CSV
    from mock_gdrive.seed.doc_filler import (
        CATEGORIES,
        generate_doc_filler_title,
        generate_doc_filler_content,
    )

    fake = Faker()
    Faker.seed(rng.randint(0, 2**32))

    non_doc_names = {
        SHEET: [
            "{topic} Tracker", "{topic} Metrics", "{topic} Data",
            "{topic} Analysis", "Budget - {topic}", "{topic} Report",
        ],
        PDF: [
            "{topic} Contract.pdf", "{topic} Report.pdf", "{topic} Invoice.pdf",
            "Receipt - {topic}.pdf", "{topic} Agreement.pdf",
        ],
        PNG: [
            "screenshot-{n}.png", "diagram-{n}.png", "mockup-{n}.png",
            "photo-{n}.png", "chart-{n}.png",
        ],
    }

    topics = [
        "Q1 Planning", "Q2 Review", "API Migration", "Customer Feedback",
        "Product Launch", "Team Sync", "Design Review", "Sprint Retro",
        "OKR Update", "Sales Pipeline", "Hiring Update", "Security Audit",
        "Cost Analysis", "Feature Request", "Bug Triage", "Release Notes",
        "Vendor Evaluation", "Training Plan", "Compliance", "Infrastructure",
        "Model Performance", "User Onboarding", "Dashboard", "Integration",
        "Testing Strategy", "Deployment", "Monitoring", "Analytics",
    ]

    folder_paths = list(folder_map.keys())
    count = 0

    for i in range(target_total):
        mime_weights = [(DOC, 0.45), (SHEET, 0.25), (PDF, 0.15), (PNG, 0.10), (CSV, 0.05)]
        mime_type = rng.choices(
            [m for m, _ in mime_weights],
            weights=[w for _, w in mime_weights],
            k=1,
        )[0]

        if mime_type == DOC:
            category = rng.choice(CATEGORIES)
            name = generate_doc_filler_title(fake, category, rng)
            content_text = generate_doc_filler_content(fake, category, name, rng)
        else:
            templates = non_doc_names.get(mime_type, non_doc_names[SHEET])
            template = rng.choice(templates)
            topic = rng.choice(topics)
            name = template.format(topic=topic, date=f"2026-{rng.randint(1,3):02d}-{rng.randint(1,28):02d}", n=i)
            content_text = None
            if mime_type in (SHEET, CSV):
                content_text = f"{name}\n\n{topic} data."

        folder_path = rng.choice(folder_paths)
        parent_id = folder_map[folder_path]

        days_ago = rng.randint(1, 365)
        created = datetime.now(timezone.utc) - timedelta(days=days_ago)
        modified = created + timedelta(days=rng.randint(0, min(days_ago, 90)))

        file_id = uuid.uuid4().hex
        f = File(
            id=file_id,
            name=name,
            mime_type=mime_type,
            parent_id=parent_id,
            owner_id=owner.id,
            last_modifying_user_id=owner.id,
            created_time=created,
            modified_time=modified,
            content_text=content_text,
            size=rng.randint(100, 500000),
        )
        db.add(f)

        db.add(Permission(
            id=uuid.uuid4().hex,
            file_id=file_id,
            role="owner",
            type="user",
            email_address=owner.email,
            display_name=owner.display_name,
        ))

        # Randomly share some files
        if rng.random() < 0.15:
            from .hierarchy import USERS
            share_user = rng.choice([u for u in USERS if u["email"] != owner.email])
            db.add(Permission(
                id=uuid.uuid4().hex,
                file_id=file_id,
                role=rng.choice(["reader", "writer", "commenter"]),
                type="user",
                email_address=share_user["email"],
                display_name=share_user["display_name"],
            ))

        count += 1

    return count
