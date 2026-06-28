# env0-mobile

`env0-mobile` contains copied task corpora used by downstream mobile and
post-training workflows.

```text
env0-mobile/
  tasks-eval/        # 60 standard eval tasks from benchflow-ai/env-0/tasks
  tasks-train/       # 1703 real task dirs, disjoint training pool
  tasks-train-mini/  # 300 real task dirs from the old mobile eval corpus
```

The root `tasks/` directory remains the small public/env0 reference set. Use
`tasks-eval` as the stable eval denominator, `tasks-train` as the broad training
pool, and `tasks-train-mini` as the compact training subset.
