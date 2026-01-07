import sys
from datetime import date

from tmngr.cli import parse_args
from tmngr.storage import plan_exists
from tmngr.commands import init, print as pr, now, done


def main():
    args = parse_args()

    # Explicit commands
    if args.command == "init":
        init.run(args.force, args.date)
        sys.exit(0)

    if args.command == "now":
        now.run()
        sys.exit(0)

    if args.command == "done":
        done.run()
        sys.exit(0)

    # Default behavior
    plan_date = getattr(args, "date", None) or date.today().isoformat()

    if not plan_exists(plan_date):
        init.run(plan_date=plan_date)
    else:
        pr.run(args)


if __name__ == "__main__":
    main()
