# Tasks Train

`tasks-train` is the disjoint generated env-0-mobile task pool. It contains 1703
GPT-5.5 xhigh-verified Google Workspace tool-use tasks across:

- `auth`
- `gcal`
- `gdoc`
- `gdrive`
- `gmail`
- `multi`

This is the broad source pool for training data generation, curriculum
construction, and sampling. It excludes every task in `tasks-eval` to keep
training and evaluation sets disjoint.

Use `tasks-eval` for the standard 60-task evaluation set. Use
`tasks-train-mini` for the smaller 300-task training subset copied from the old
strong-model-verified mobile eval corpus.
