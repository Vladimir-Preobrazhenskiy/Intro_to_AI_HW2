# README

This folder is the workspace for the academic course **AI and Python Programming:
AI HW2**. It teaches how to work with AI **agents**: configure them
as Markdown files, prompt them, permission them, verify their output, and combine
them into teams. Python is the working domain; the language itself is taught in
*Development Essentials*. It is a teaching project, not a software repository.

The task for AI to automate was the creation of backups of the folder /project - so they did
Unfortunately, chats with .chat were working quite poorly – failing with error and not providing / commands even after restart of opencode and Jupyterhub session, so for commands I used Opencode in terminal – it worked perfectly, however I could not save it as .chat

## Project layout

- `scripts/` — draft modules agents produce for the user to run.
  - `backup_project.py` — archives the `project/` folder into `backups/` as a timestamped zip.
- `project/` — a pet project with some code (`Vovas_code_ver1.ipynb`).
- `backups/` — timestamped zip backups created by `scripts/backup_project.py`.
- `.opencode/agent/*.md` — the assistant team (each agent is one Markdown file).
- `.opencode/command/*.md` — reusable prompts that point at agents.
- `*.chat` — saved chat sessions with AI agents.

## Working rules for any assistant in this project

### Environment constraints
- Python 3.12 with standard data-science libraries (numpy, pandas, matplotlib,
  scikit-learn, PyTorch, TensorFlow/Keras).
- No internet access inside the sandbox.
- All work must stay within the current working directory.

### Working conventions
- The user is a learner, not an expert programmer: explain the *why* next to
  every change and keep drafts short, clear, and reproducible.
- Verify changes by executing notebook cells (`.ipynb`) or running scripts directly.
- Read files before editing them.

### Code style
- Python: PEP 8, type hints encouraged.
- Keep code short and clean.

### File safety
- Never delete or overwrite existing files without explicit confirmation.
- Do not use destructive commands (`rm`, `truncate`, `delete`).
- Never put secrets or tokens in code, prompts, or committed files.

### Communication
- Be concise and to the point.
- When presenting code, use minimal, targeted snippets.

## Agents

Agent files take effect after OpenCode is restarted (loaded once at startup).

| Agent file | Description |
|---|---|
| `.opencode/agent/agent-command-builder.md` | Designs, improves, and reviews agents and commands. |
| `.opencode/agent/Python_expert.md` | All-in-one Python helper — writes functions, documents code, and debugs errors. |
| `.opencode/agent/git-explorer.md` | Reads a git repository with read-only commands and explains it. |

## Commands

Reusable prompts live in `.opencode/command/`. Each points at an agent that
handles the task.

| Command file | Description | Agent |
|---|---|---|
| `.opencode/command/debugging.md` | Analyse a Python error or buggy function and propose a fix. | `Python_expert` |
| `.opencode/command/doc-writing.md` | Add docstrings and documentation to existing Python code. | `Python_expert` |
| `.opencode/command/function-writing.md` | Write a new Python function from a short specification. | `Python_expert` |
