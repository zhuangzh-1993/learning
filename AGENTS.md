# Instructions for pi

Commit messages follow the rules in `.pi/ai-git-commit.json`, field
`instructions`. That file is read directly by the `/git-commit` extension and
by nothing else, so a message written by hand has to go through it as well.
Read it before writing a commit message: the rules live in one place on
purpose, and this file is only the pointer to them.

The mechanical half of those rules is checked by a `commit-msg` hook, so a
message never reaches history with a type prefix, an over-long line or a
marketing word. Install it once per clone:

```sh
pre-commit install --hook-type commit-msg
```

The hook cannot see whether the body explains why, or whether a commit is one
logical change; that stays on the author.
