# AGENTS.md

## Repository Guidelines

### Project Structure

Core logic lives under `samplepath/` (`cli.py`, `metrics.py`, `limits.py`,
`csv_loader.py`, `plots/`). Treat this package as the source of truth for all features.
Documentation lives in `docs/`; examples in `examples/`. Generated artifacts (`charts/`,
`dist/`, `htmlcov/`, `coverage.xml`) should not be modified. Tests mirror the source
tree under `test/`.

Agent must not modify any file outside the scope of the task being executed.

______________________________________________________________________

## Agent Task Workflow

Tasks are defined in `tasks/Task.md`. Each task has:

- an **ID**
- a **Name**
- a **Branch**
- a **Specification block**

Agent must:

1. Locate the task block matching the given **Task ID**.
2. Use only that block as the authoritative task description.
3. Modify **only** the files referenced or required by that task.
4. If the task-specified branch does not exist, create it from the latest `main`.
5. Make only the minimal changes needed to complete the task and nothing else.

### Execution Protocol

- Before making any code changes, Agent must present a step-by-step plan and wait for
  explicit approval.
- After approval, apply patches only to the task branch.
- After applying patches, stop and wait for review before making additional edits.
- Agent must not open pull requests unless explicitly instructed.

### Commit Requirements

Use the task **ID** in commit messages. Use the task **Name** when reporting work being
done. When merging to `main`, prefer a squash merge. Merge commit message format:

```
[Task ID]: (Task Name): Merge <branch name> to main
```

______________________________________________________________________

## Documentation Workflow

Pandoc converts Markdown to HTML using the tooling in `docs/build/`. Before committing
Markdown changes:

1. Run `pre-commit`.
2. If `mdformat` reports changes, present them for review before committing.
3. Do not rewrite any YAML front matter in markdown files unless explicitly instructed.

______________________________________________________________________

## Build, Test, and Development Commands

Provision environment:

```
uv sync --all-extras
```

Run CLI checks:

```
uv run samplepath examples/polaris/csv/work_tracking.csv --help
```

Run tests:

```
uv run pytest
```

### Formatting and Linting (canonical order)

Agent must always run pre-commit before committing any code.

```
pre-commit run
```

IF pre-commit checks modify files wait for approval before committing the code.

______________________________________________________________________

## Coding Style & Naming Conventions

Follow PEP 8 with explicit type hints. Snake_case for modules; CamelCase for public
classes. CLI flags use kebab-case. Avoid side effects at module scope. Keep helpers near
their call sites.

______________________________________________________________________

## Testing Guidelines

Add tests under `test/` mirroring the source tree. Before implementing code changes
propose one or more failing tests that will verify the task specification and wait for
review. Use one assertion per test. Use parametrized tests for scenario coverage.
Fixtures should be deterministic. Agent may modify existing tests only when required by
the task’s acceptance criteria. Always present modifications of existing tests for
review before making any changes.

# End of file
