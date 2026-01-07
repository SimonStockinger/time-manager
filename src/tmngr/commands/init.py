from datetime import date
from tmngr.model import Slot, Todo, DayPlan
from tmngr.storage import save_plan, plan_exists
from tmngr.slots import SLOTS

def run(force=False, plan_date=None):
    plan_date = plan_date or date.today().isoformat()

    if plan_exists(plan_date) and not force:
        if input("Plan exists. Overwrite? [y/N]: ").lower() != "y":
            return

    slots = []

    for time in SLOTS:
        print(f"{time}:")
        topic = input("Topic: ").strip()
        if not topic:
            continue

        todos = []
        while True:
            text = input("Todo: ").strip()
            if not text:
                break
            todos.append(Todo(text))

        slots.append(Slot(time, topic, todos))

    save_plan(DayPlan(plan_date, slots))
