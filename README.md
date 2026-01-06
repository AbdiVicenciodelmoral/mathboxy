# Math Box Prototype (PyQt6)

A desktop puzzle game prototype inspired by grid-based logic/math puzzles (think “math cages” / grouped cells).  
The goal is to fill an **N×N** grid with numbers while satisfying the puzzle’s grouping constraints.

> This project is actively being developed with a collaborator. Expect changes and improvements over time.

---

## Table of Contents
- [What is the game?](#what-is-the-game)
- [How to play](#how-to-play)
- [Project status](#project-status)
- [How it’s built](#how-its-built)
- [Getting started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Create and use a virtual environment (recommended)](#create-and-use-a-virtual-environment-recommended)
  - [Install dependencies](#install-dependencies)
  - [Run the app](#run-the-app)
- [Developer notes](#developer-notes)
- [Contributing](#contributing)
- [License](#license)

---

## What is the game?
**Math Box** is a grid-based puzzle. Each puzzle contains:
- An **N×N grid**
- **Groups (cages)** that partition the grid into regions (the generator creates these)
- (Planned) math constraints for each group such as a **target number** and **operation** (e.g., `12×`, `7+`, etc.)

The game will eventually show only the playable puzzle grid.  
During development, we also support debug views like showing group outlines and solution numbers.

---

## How to play
> Rules are still evolving as the generator and UI are developed. The intended gameplay is:

1. Fill the grid with numbers (typically `1..N`).
2. (Planned) Each row/column must satisfy constraints (e.g., no duplicates) depending on the final rule set.
3. Each **group/cage** must satisfy its math rule (target + operation).
4. Solve until the entire grid is valid.

---

## Project status
✅ Basic PyQt6 grid window implemented  
✅ Solution generation and grouping (prototype generator)  
🚧 Group boundary rendering (in-progress)  
🚧 Final puzzle rules, input UI, validation, and gameplay loop (planned)

---

## How it’s built
- **Language:** Python 3
- **UI:** [PyQt6](https://pypi.org/project/PyQt6/)
- **Core modules:**
  - `main.py` – app entry point (creates generator and launches UI)
  - `grid_window.py` – renders the grid in a `QTableWidget`
  - `puzzle_generator.py` – generates solution grid and groupings (uses `random`)

### Current imports (not exhaustive)
- `PyQt6.QtWidgets` (`QApplication`, `QMainWindow`, `QTableWidget`, `QTableWidgetItem`)
- `PyQt6.QtCore` (`Qt`)
- `random`
- `enum` (`Enum`, `auto`)
- `__future__` annotations

---

## Getting started

### Prerequisites
- **Python 3.10+** recommended  
  Check your version:
  ```powershell
  python --version

### (Optional but recommended) Git installed

Check that Git is installed by running:

```powershell
git --version

## Create and use a virtual environment (recommended)

### Why use a virtual environment?

A virtual environment isolates your project dependencies from your system Python.  
This prevents version conflicts and makes it easier for collaborators to match the same setup.

### Windows (PowerShell)

From the project root folder:

```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then try activating again:

```
.\.venv\Scripts\Activate.ps1
```

### macOS / Linux (bash/zsh)

```
python3 -m venv .venv
source .venv/bin/activate
```


## Install dependencies

### Install PyQt6

With the virtual environment activated:

```
python -m pip install --upgrade pip
pip install PyQt6
```

### (Recommended) Freeze dependencies

After installing everything you use, generate a `requirements.txt` so collaborators can install easily:

```
pip freeze > requirements.txt
```

Then others can do:

```
pip install -r requirements.txt
```

---

## Run the app

From the project root:

```
python main.py
```

---

## Developer notes

### View modes (debugging)

The UI supports multiple render modes for development/testing:

- `GAME` – only the playable grid (final intended view)
- `GROUPS` – group/cage visuals only (no numbers)
- `GROUPS_AND_NUMBERS` – groups + solution numbers (debug)

These are defined in `grid_window.py` using an Enum `ViewMode`.

---

## Contributing

This is a collaborative project.

Suggested workflow:

1. Create a new branch for each feature:

```
git checkout -b feature/<short-name>
```

2. Commit often with clear messages.

3. Push your branch and open a Pull Request.

### Code style

- Keep functions small and well-commented
- Prefer readable code over clever code
- Add simple tests or debug helpers where helpful

---

## License

TBD (choose a license when ready — e.g., MIT).

---

### Two quick upgrades I recommend adding right now

1) **Add a `requirements.txt`** once you confirm the dependencies:
- Activate venv
- Install PyQt6
- Freeze dependencies

```
pip install PyQt6
pip freeze > requirements.txt
```

2) Add a `.gitignore` (Python + venv) if you haven’t already:

```
__pycache__/
*.pyc
.venv/
venv/
.env
.DS_Store
.idea/
.vscode/
```
