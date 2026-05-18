# AGENT.md

Global rules for all work on this project. Read before every task.

**Tradeoff**: These guidelines bias toward caution over speed. For trivial tasks, use judgment.

---

## 1. Think Before Coding

Don't assume. Don't hide confusion. Surface tradeoffs.

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them — don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

Minimum code that solves the problem. Nothing speculative.

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: *"Would a senior engineer say this is overcomplicated?"* If yes, simplify.

## 3. Surgical Changes

Touch only what you must. Clean up only your own mess.

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it — don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that **your** changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

Define success criteria. Loop until verified.

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

---

## 5. Environment

- All commands run inside conda env `Master_thesis`. Check first via `conda env list`; if absent, create with `conda create -n Master_thesis python=3.11 -y`. Never install packages or run scripts outside this env.

## 6. GitHub

- Repo: `https://github.com/Imcheatingbro/Master-thesis.git` (public).
- Push after each completed task. Commit message format: `[module] short description` in Chinese.
- One commit = one logical change. No mixed commits.

## 7. Code Standards

- Type hints required on all public functions.
- Module-level docstring required, mapping the file to its spec section.
- No `print` — use `logging`. No `except: pass` — log and handle explicitly.

## 8. Testing

- Run `pytest` for the affected module after every change. Do not commit on red.
- New logic needs a new test. Bug fix needs a regression test.

## 9. Communication

- All commits, comments, docstrings, and `reports/LESSONS.md` entries in **Chinese**.
- If a spec is unclear or you must deviate from it, stop and ask the project author. Do not guess.
- Log every pitfall, design tradeoff, and deviation in `reports/LESSONS.md` before pushing.

---

**These guidelines are working if**: fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.
