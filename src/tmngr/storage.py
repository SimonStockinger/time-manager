import json
import os
from pathlib import Path
from tmngr.model import DayPlan, Slot, Todo

DATA_DIR = os.environ.get(
    "TMNGR_DATA_DIR",
    os.path.expanduser("~/.local/share/tmngr")
)

def ensure_data_dir():
    Path(DATA_DIR).mkdir(parents=True, exist_ok=True)

def plan_path(date: str) -> Path:
    return Path(DATA_DIR) / f"{date}.json"

def plan_exists(date: str) -> bool:
    return plan_path(date).exists()

def save_plan(plan: DayPlan):
    ensure_data_dir()
    data = {
        "date": plan.date,
        "slots": [
            {
                "time": s.time,
                "topic": s.topic,
                "todos": [
                    {"text": t.text, "done": t.done}
                    for t in s.todos
                ]
            } for s in plan.slots
        ]
    }
    with open(plan_path(plan.date), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_plan(date: str) -> DayPlan:
    with open(plan_path(date), "r", encoding="utf-8") as f:
        raw = json.load(f)

    slots = []
    for s in raw.get("slots", []):
        todos = [Todo(t["text"], t.get("done", False)) for t in s["todos"]]
        slots.append(Slot(s["time"], s["topic"], todos))

    return DayPlan(raw["date"], slots)
