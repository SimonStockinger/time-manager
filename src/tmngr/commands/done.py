from datetime import date
from tmngr.slots import current_slot
from tmngr.storage import load_plan, save_plan

def run():
    slot_time = current_slot()
    if not slot_time:
        print("No active slot.")
        return

    plan = load_plan(date.today().isoformat())
    for s in plan.slots:
        if s.time == slot_time:
            if not s.todos:
                print("No todos.")
                return

            print(f"{s.time}: {s.topic}")
            for i, t in enumerate(s.todos, 1):
                mark = "[x]" if t.done else "[ ]"
                print(f"{i}) {mark} {t.text}")

            sel = input("Toggle todo: ").strip()
            if not sel.isdigit():
                return

            idx = int(sel) - 1
            if 0 <= idx < len(s.todos):
                s.todos[idx].done = not s.todos[idx].done
                save_plan(plan)
            return
