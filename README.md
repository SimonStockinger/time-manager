# tmngr – Terminal Time Manager

**README still under construction**

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)

`tmngr` is a minimal command-line time and task manager designed for students. 
It helps you plan your day in time slots, track tasks, and mark progress directly from the terminal.

Currently written in Python, designed for Linux (especially Arch Linux), and easily installable via `pipx`.

---
## Features

- Plan your day in **predefined time slots** (e.g., `07-08`, `08-09`, …, `22-23`)  
- Add **topics** and multiple **todos** per slot  
- Persist tasks in **JSON files** for each day  
- Track completion with `[ ]` (incomplete) and `[x]` (done)  
- Commands:
  - `tmngr init` – create or update today's plan  
  - `tmngr print` – display your plan  
  - `tmngr now` – show the current slot  
  - `tmngr done` – mark/unmark todos as done  
- Optional JSON output for automation or scripting

Running `tmngr` without arguments calls `init` if run for the first time of the day. Else `print` is executed.

---

## Installation

Recommended via **pipx**:

```bash
# Install pipx if needed
sudo pacman -S python-pipx
pipx ensurepath

# Install tmngr in editable mode for development
pipx install --editable /path/to/tmngr-project
```

Or uninstall/reinstall if already installed:
```bash
pipx uninstall tmngr
pipx install --editable /path/to/tmngr-project
```

## Usage
### Initialize the day
```bash
tmngr init
```

Follow the interactive prompts:
```
07-08: Overview
Todo: Review plan
Todo: Make tea
Todo: 
08-09: Operating Systems
Todo: Solve past exam 20/22
Todo:
```

Leave the input empty to move to the next slot.

### Print the plan

```bash
tmngr print
tmngr print --date 2026-01-07
tmngr print --json
```
Sample output:
```
07-08: Overview
[ ] Review plan
[ ] Make tea

08-09: Operating Systems
[ ] Solve past exam 20/22
```

### Show the current slot

```bash
tmngr now
```

Displays the current time slot and its tasks with status.

### Mark/unmark tasks as done

## Data storage

## Project structure

## Development

## License

MIT License – see LICENSE file.

# Contributing
