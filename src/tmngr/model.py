from dataclasses import dataclass
from typing import List

@dataclass
class Todo:
    text: str
    done: bool = False

@dataclass
class Slot:
    time: str
    topic: str
    todos: List[Todo]

@dataclass
class DayPlan:
    date: str
    slots: List[Slot]
