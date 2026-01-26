import argparse

def parse_args():
    parser = argparse.ArgumentParser(prog="tmngr")
    sub = parser.add_subparsers(dest="command")

    # init
    init_p = sub.add_parser("init")
    init_p.add_argument("--force", action="store_true")
    init_p.add_argument("--date")

    # print
    print_p = sub.add_parser("print")
    print_p.add_argument("--json", action="store_true")
    print_p.add_argument("--date")

    # now, done
    sub.add_parser("now")
    sub.add_parser("done")

    # todo
    todo_p = sub.add_parser("todo")
    todo_p.add_argument(
        "task",
        nargs="*",
        help="Neue Aufgabe oder 'done' für Löschmodus"
    )

    return parser.parse_args()
