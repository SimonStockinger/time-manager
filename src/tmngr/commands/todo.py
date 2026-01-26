import json
import os
from pathlib import Path
from tmngr.model import Todo

DATA_DIR = os.environ.get(
    "TMNGR_DATA_DIR",
    os.path.expanduser("~/.local/share/tmngr")
)
TODO_FILE = Path(DATA_DIR) / "global_todos.json"

def ensure_data_dir():
    Path(DATA_DIR).mkdir(parents=True, exist_ok=True)

def load_todos():
    ensure_data_dir()
    if not TODO_FILE.exists():
        return []
    with open(TODO_FILE, "r", encoding="utf-8") as f:
        raw = json.load(f)
    return [Todo(t["text"]) for t in raw]

def save_todos(todos):
    ensure_data_dir()
    data = [{"text": t.text} for t in todos]
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def run(arguments=""):
    todos = load_todos()
    arg = arguments.strip().lower()

    if arg == "":
        print_todo(todos)
    elif arg == "done":
        remove_todo(todos)
    else:
        new_todo(todos, arguments)

    save_todos(todos)


def print_todo(todos):
    if not todos:
        print("Keine Todos vorhanden.")
        return

    print("Generelle Todo-Liste:")
    print("-------------------")
    for i, t in enumerate(todos, 1):
        print(f"{i}) {t.text}")


def remove_todo(todos):
    if not todos:
        print("Keine Todos vorhanden.")
        return

    print("Welche Todos entfernen?")
    for i, t in enumerate(todos, 1):
        print(f"{i}) {t.text}") 

    sel = input("Nummer zum Löschen (Enter zum Abbrechen): ").strip()
    if not sel.isdigit():
        print("Abgebrochen.")
        return

    idx = int(sel) - 1
    if 0 <= idx < len(todos):
        removed = todos.pop(idx)
        print(f"Todo '{removed.text}' entfernt.")


def new_todo(todos, text: str):
    todos.append(Todo(text.strip()))
    print(f"Todo hinzugefügt: {text.strip()}")
