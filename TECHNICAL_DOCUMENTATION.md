# Elysium Station – Technical Documentation

## Where the Code Is Hosted

- Repository: `https://github.com/vrajkumarpatel/Elysium_Adventure_Game.git`
- Default branch: `main`
- Root layout: `main.py`, `player.py`, `chapter1.py`–`chapter5.py`, `assets/`, `README.md`

## External Services

- None. The game runs entirely on Python’s standard library.

## Languages and Technologies

- Python 3.8+
- Standard library only (no third‑party dependencies)

## System Requirements and Supported Applications

- OS: Windows, macOS, or Linux
- Python: 3.8 or higher (`python --version`)
- Terminal/IDE: VS Code, PyCharm, Thonny, or system terminal
- Optional: ANSI color support in the terminal; set `USE_COLOR = False` in `player.py` if colors render oddly (`player.py:49`).

Maintenance and troubleshooting:
- If ASCII art does not show, verify files in `assets/` (e.g., `assets/title.txt`).
- If a chapter returns an unexpected id, the game exits safely and prints a message (`main.py:68`).
- If color output causes artifacts, disable color (`player.py:49`).

## Coding and Naming Conventions

- `snake_case` for variables and functions
- `PascalCase` for class names
- One chapter per file with entry functions like `run_chapter1()` (`chapter1.py:36`).
- Game entry point `main()` in `main.py` (`main.py:18`).

## How to Run / Build / Deploy

- Run locally:
  - `python main.py`
- Build: Not required; this is a pure Python script project.
- Deploy:
  - Host the repository on GitHub (push to `main`).
  - Optionally package a zip for assignment submission (see below).

## Architecture Overview

- `main.py` – Entry point; displays title art, asks for player name, loops chapters (`main.py:18`, `main.py:50`).
- `player.py` – `Player` class with inventory, status, flags; UI helpers `banner`, `divider`, `show_hud`, `choose`, `clear_screen`, `print_art` (`player.py:10`, `player.py:80`, `player.py:103`, `player.py:133`, `player.py:139`).
- `chapter1.py`–`chapter5.py` – Narrative and choice handling per chapter; each returns the next chapter id or `win`/`fail`/`quit` (`chapter1.py:36`).
- `assets/` – ASCII art text files for title and scenes.

Chapter flow:
- `main.py` maps chapter ids to functions and loops until an ending (`main.py:39`, `main.py:50`).

## How to Start the Program

- From the project root:
  - `python main.py`
- When prompted, enter your investigator name and follow on‑screen choices.

## Packaging for Assignment Submission

- Include the entire game plus this technical documentation in a single zip.
- The repository should also host the documentation non‑zipped (commit `TECHNICAL_DOCUMENTATION.md` to `main`).
