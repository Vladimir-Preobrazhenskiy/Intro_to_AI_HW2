---
description: Write a new Python function from a short specification.
agent: Python_expert
---

## Task: Write a Python function

The user gives you a specification — inputs, output, and expected behaviour.

1. Read the target file first if one is named; otherwise write a standalone function.
2. Write clean, runnable Python with:
   - Type hints on every parameter and the return value.
   - A one-line docstring describing what the function does.
   - 2–3 `assert` statements at the bottom that prove correctness.
3. Handle edge cases explicitly: empty list, 0, None, negative numbers.
4. Never use libraries that are not already imported in the project.
5. If the user names a file, append the function there; otherwise propose a new file.
