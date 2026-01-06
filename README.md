# MathBoxy 🧩

A desktop puzzle game prototype built with Python and PyQt6.

MathBoxy is a grid-based logic/math puzzle inspired by games that use **grouped cells (cages)** with constraints.  
The project is currently in active development and is being built collaboratively.

---

## Table of Contents
- [What is the game?](#what-is-the-game)
- [How to play](#how-to-play)
- [Project status](#project-status)
- [How it’s built](#how-its-built)
- [Getting started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Virtual environment (recommended)](#virtual-environment-recommended)
  - [Install dependencies](#install-dependencies)
  - [Run the app](#run-the-app)
- [Developer notes](#developer-notes)
- [Contributing](#contributing)
- [License](#license)

---

## What is the game?
**MathBoxy** is an **N×N grid-based puzzle game**.

Each puzzle consists of:
- A square grid (e.g. 4×4, 6×6)
- Groups (also called *cages*) that divide the grid into regions
- (Planned) mathematical constraints per group, such as a target number and operation

The player’s goal is to fill in the grid so that all constraints are satisfied.

---

## How to play
> The exact rules are still evolving as the generator and UI are developed.

Planned gameplay:
1. Fill each cell with a number (typically `1..N`)
2. (Planned) Rows and columns must follow validity rules (e.g., no duplicates)
3. Each group/cage must satisfy its math rule
4. The puzzle is solved when the entire grid is valid

---

## Project status
- ✅ PyQt6 grid UI implemented
- ✅ Solution grid generation
- ✅ Grouping (cage) generation (logic side)
- 🚧 Visual cage boundaries (in progress)
- 🚧 Gameplay input and validation (planned)

---

## How it’s built

### Language
- **Python 3**

### Libraries
- **PyQt6** – GUI framework
- **random** – puzzle generation
- **enum** – render/view modes
- **__future__ annotations** – forward-compatible typing

### Key files
- `main.py` – Application entry point
- `grid_window.py` – UI grid rendering and view modes
- `puzzle_generator.py` – Puzzle and grouping generation logic

---

## Getting started

### Prerequisites
- **Python 3.10+** recommended  
  Check your version:
  ```powershell
  python --version
(Optional but recommended) Git:

powershell
Copy code
git --version
Virtual environment (recommended)
Why use a virtual environment?
A virtual environment:

Keeps project dependencies isolated

Prevents version conflicts

Makes collaboration easier and reproducible

Windows (PowerShell)
From the project root folder:

powershell
Copy code
python -m venv .venv
.\.venv\Scripts\Activate.ps1
If PowerShell blocks activation, run:

powershell
Copy code
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
Then activate again:

powershell
Copy code
.\.venv\Scripts\Activate.ps1
macOS / Linux (bash/zsh)
bash
Copy code
python3 -m venv .venv
source .venv/bin/activate
Install dependencies
With the virtual environment activated:

powershell
Copy code
python -m pip install --upgrade pip
pip install PyQt6
(Recommended) Freeze dependencies
After installing everything you use:

powershell
Copy code
pip freeze > requirements.txt
Other contributors can then install dependencies with:

powershell
Copy code
pip install -r requirements.txt
Run the app
From the project root:

powershell
Copy code
python main.py
Developer notes
View modes (debugging)
The UI supports multiple render modes for development:

GAME – Only the playable grid (final intended view)

GROUPS – Group/cage visuals only

GROUPS_AND_NUMBERS – Groups + solution numbers (debug)

These modes are defined in grid_window.py using an Enum called ViewMode.

Contributing
This is a collaborative project.

Suggested workflow
Create a new branch for each feature:

powershell
Copy code
git checkout -b feature/your-feature-name
Commit changes with clear messages

Push your branch and open a Pull Request

Code style
Keep functions small and well-commented

Prefer readable code over clever code

Add simple debug helpers where helpful

License
TBD (choose a license when ready, e.g. MIT).

yaml
Copy code

---

## ✅ How to add it via the GitHub browser (no terminal)

1. Go to:  
   👉 https://github.com/AbdiVicenciodelmoral/mathboxy
2. Click **Add a README** (or edit the existing one)
3. **Paste everything above**
4. Click **Commit changes**

GitHub will render it perfectly.

---

### Why this version works
- ✔ Proper `#` headers
- ✔ Proper fenced code blocks (```powershell / ```bash)
- ✔ No stray “Copy code” text
- ✔ GitHub-friendly Markdown

If you want, next we can:
- Add screenshots to the README
- Add a roadmap section
- Add badges (Python version, status)
- Add a CONTRIBUTING.md for your friend




