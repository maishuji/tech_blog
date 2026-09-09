# Repository instructions

These instructions apply throughout this repository.

## Branch naming

Use this format for new work branches:

```text
<type>/<short-description>
```

- Choose a type from the commit types below that matches the branch's purpose.
- Use lowercase letters, numbers, and hyphens in the description (kebab-case).
- Keep the description short and specific to the change.
- When referencing an issue, put its number before the description, for example
  `fix/123-pi-ssh-key-path`.

Examples: `feat/article-search`, `fix/pi-ssh-key-path`,
`docs/branch-and-commit-conventions`.

Conventional Commits defines commit messages; the branch format above is this
repository's convention using the same types.

## Commit messages

Follow [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/).

```text
<type>[optional scope][!]: <description>

[optional body]

[optional footers]
```

- Use `feat` for features and `fix` for bug fixes.
- Other repository types are `docs` (documentation), `refactor` (restructuring
  without changing behavior), `perf` (performance), `test` (tests), `build`
  (build tooling or dependencies), `ci` (CI configuration), `style` (formatting),
  `chore` (maintenance), and `revert` (reverting changes).
- Use lowercase types and scopes. Choose a scope when it adds useful context,
  such as `deploy`, `tags`, or `import`.
- Put no space before the colon and one space after it: `fix(deploy): ...`.
- Write a concise, imperative description, such as "expand" or "add", without
  a trailing period. Aim for a subject of 72 characters or fewer.
- Separate the subject, optional body, and optional footers with blank lines.
  Use the body to explain the reason for the change when needed.
- Mark breaking changes with `!` before the colon or a
  `BREAKING CHANGE: <explanation>` footer. Explain the impact and migration.
- Keep each commit focused on one logical change. Split unrelated changes into
  separate commits and describe the actual changes in each message.

Examples:

```text
fix(deploy): expand home directory in Pi SSH key paths
docs: document branch and commit conventions
feat(tags): add tag filtering
feat(import)!: require explicit source configuration
```
