# Dispatcher edits on a Delta Courier parcel: undo and redo are two stacks.
import csv
from stack import Stack

rows = list(csv.DictReader(open("../../data/packages.csv")))
parcel = next(r for r in rows if r["status"] == "at hub")
status = parcel["status"]
undo, redo = Stack(), Stack()


def edit(new):
    global status
    undo.push(status); status = new
    while not redo.is_empty():
        redo.pop()          # a new edit clears the redo pile


def undo_last():
    global status
    redo.push(status); status = undo.pop()


def redo_last():
    global status
    undo.push(status); status = redo.pop()


print(f"{parcel['tracking']} start: {status}")
edit("in transit"); edit("delivered")
print(f"after 2 edits: {status} | undo {len(undo)} redo {len(redo)}")
undo_last()
print(f"undo: {status} | undo {len(undo)} redo {len(redo)}")
redo_last()
print(f"redo: {status} | undo {len(undo)} redo {len(redo)}")
