# AGENTS.md

This is a student workspace for the **Intro to AI** course (Homework 2).  
The focus is on AI script writing and debugging.


This folder is the workspace for the academic course *AI and Python Programming:
AI HW2*. It teaches how to work with AI **agents**: configure them
as Markdown files, prompt them, permission them, verify their output, and combine
them into teams. Python is the working domain; the language itself is taught in
*Development Essentials*. It is a teaching project, not a software repository.

## Project layout

- `scripts/` - draft modules agents produce for the user to run.
- `project/` - my pet project with some code.
- `backups/` - the backups of my per project
- `.opencode/agent/*.md` - the assistant team (each agent is one Markdown file).
- `.opencode/command/*.md` - reusable prompts that point at agents.

## Working rules for any assistant in this project

### Environment constraints
- Python 3.12 with standard data-science libraries (numpy, pandas, matplotlib, scikit-learn, PyTorch, TensorFlow/Keras).
- No internet access inside the sandbox.
- All work must stay within the current working directory.

### Working conventions
- Verify changes by executing notebook cells (`.ipynb`) or running scripts directly.
- Read files before editing them.

### Code style
- Python: PEP 8, type hints encouraged.
- Keep code short and clean.

### File safety
- Never delete or overwrite existing files without explicit confirmation.
- Do not use destructive commands (`rm`, `truncate`, `delete`).

### Communication
- Be concise and to the point.
- When presenting code, use minimal, targeted snippets.

## Agents

- `.opencode/agent/agent-command-builder.md` - designs, improves, and reviews agents and commands.
- `.opencode/agent/Python-expert.md` - debugs Python and write algorithms.
- `.opencode/agent/git-explorer.md` - explores git.

Agent files take effect after OpenCode is restarted (loaded once at startup).
Reusable prompts live in `.opencode/command/`.