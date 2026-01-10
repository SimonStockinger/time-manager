from datetime import date
from datetime import datetime
from tmngr.storage import load_plan

def run(args):
    plan_date = getattr(args, "date", None) or date.today().isoformat()
    plan = load_plan(plan_date)

    if getattr(args, "json", False):
        import json
        print(json.dumps({
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
        }, indent=2, ensure_ascii=False))
        return

    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("-------------------")
    for s in plan.slots:
        print(f"{s.time}: {s.topic}")
        for t in s.todos:
            mark = "[x]" if t.done else "[ ]"
            print(f"{mark} {t.text}")
