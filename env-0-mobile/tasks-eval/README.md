# Tasks Eval

`tasks-eval` is the 300-task strong-model-verified evaluation set.
It is intentionally excluded from `tasks-train`.

The task contents are real directories, not symbolic links, to keep the
evaluation set self-contained and easy to inspect. The selection is balanced as
50 tasks each across:

- `auth`
- `gcal`
- `gdoc`
- `gdrive`
- `gmail`
- `multi`
