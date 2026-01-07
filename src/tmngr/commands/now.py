from datetime import date
from tmngr.slots import current_slot
from tmngr.storage import load_plan

def run():
    slot_time = current_slot()
    if not slot_time:
        return

    plan = load_plan(date.today().isoformat())
    for s in plan.slots:
        if s.time == slot_time:
            print(f"NOW {s.time}: {s.topic}")
            for t in s.todos:
                mark = "[x]" if t.done else "[ ]"
                print(f"{mark} {t.text}")
            return

    print(f"NOW {slot_time}: (no plan)")
