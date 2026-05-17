# AGENT.md

Global rules for all work on this project. Read before every task.

## Environment
- All commands run inside conda env `Master_thesis`. Check first via `conda env list`; if absent, create with `conda create -n Master_thesis python=3.11 -y`. Never install packages or run scripts outside this env.

## GitHub
- Repo: `https://github.com/Imcheatingbro/Master-thesis.git` (public).
- Push after each completed task. Commit message format: `[module] short description` in Chinese.
- One commit = one logical change. No mixed commits.

## Code Discipline
- **Do not refactor unrelated code.** Touch only files the current task requires. If you spot something worth refactoring, note it in `reports/LESSONS.md` under "TODO" — do not act on it.
- **Do not modify unrelated files.** This includes configs, other modules, notebooks, and existing tests outside the task scope.
- **Keep code minimal.** If 50 lines suffice, do not write 200. Prefer standard library and direct solutions over frameworks and abstractions. No premature OOP, no speculative parameters, no "just in case" branches.
- Type hints required on all public functions. Module-level docstring required, mapping the file to its spec section.
- No `print` — use `logging`. No `except: pass` — log and handle explicitly.

## Testing
- Run `pytest` for the affected module after every change. Do not commit on red.
- New logic needs a new test. Bug fix needs a regression test.

## Communication
- All commits, comments, docstrings, and `LESSONS.md` entries in Chinese.
- If a spec is unclear or you must deviate from it, stop and ask the project author. Do not guess.
- Log every pitfall, design tradeoff, and deviation in `reports/LESSONS.md` before pushing.
