# Tasks Train Mini

`tasks-train-mini` is the 300-task strong-model-verified mobile corpus copied
from `benchflow-ai/env-0/env-0-mobile/tasks-eval`.

The task contents are real directories, not symbolic links, to keep the subset
self-contained and easy to inspect. Dockerfile COPY paths are adjusted for the
`env-0-mobile/tasks-train-mini` location.

This set is balanced as 50 tasks each across:

- `auth`
- `gcal`
- `gdoc`
- `gdrive`
- `gmail`
- `multi`

Use `tasks-eval` for the 60-task standard evaluation denominator and
`tasks-train` for the full 1703-task disjoint training pool.
