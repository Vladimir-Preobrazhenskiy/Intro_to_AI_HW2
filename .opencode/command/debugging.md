---
description: Analyse a Python error or buggy function and propose a fix.
agent: Python_expert
---

## Task: Debug Python code

The user gives you broken code and a traceback, or points to a buggy file.

1. Explain the **root cause** in one beginner-friendly sentence (e.g. «ты попросил 5-й элемент списка, в котором всего 3»).
2. Point to the exact line or expression that is wrong.
3. Provide the corrected code and 1–2 `assert` examples that now pass.
4. Add a **prevention note** — what to check next time so this bug does not repeat.
5. If the traceback hints at a missing import, assume standard library only.
6. When asked, save the fix proposal to `reports/<name>_debug.md`.
