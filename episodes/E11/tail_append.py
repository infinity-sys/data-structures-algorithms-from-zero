import csv

class Box:
    def __init__(self, cargo, next=None):
        self.cargo, self.next = cargo, next

rows = list(csv.DictReader(open("../../data/packages.csv")))

head, hops = Box(rows[0]["tracking"]), 0     # head only
for r in rows[1:]:
    b = head
    while b.next is not None:        # walk to the last box
        b, hops = b.next, hops + 1
    b.next = Box(r["tracking"])
print(f"append 600, head only: {hops:,} hops")

head = tail = Box(rows[0]["tracking"])       # head AND tail
notes = 0
for r in rows[1:]:
    tail.next = Box(r["tracking"])   # note 1: old last box -> new
    tail = tail.next                 # note 2: tail moves to new
    notes += 2
print(f"append 600, with tail: 0 hops, {notes:,} notes")
print(f"last parcel: {tail.cargo}")
