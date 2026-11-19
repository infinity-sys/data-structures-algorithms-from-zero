import csv

class Box:
    def __init__(self, cargo, next=None):
        self.cargo, self.next = cargo, next

class DBox:
    def __init__(self, cargo):
        self.cargo = cargo
        self.next = None
        self.prev = None

rows = list(csv.DictReader(open("../../data/packages.csv")))
assert len(rows) == 600

# singly + tail: delete the last parcel
head = Box(rows[0]["tracking"]); cur = head
for r in rows[1:]:
    cur.next = Box(r["tracking"]); cur = cur.next
tail = cur
prev, hops = head, 0
while prev.next is not tail:
    prev = prev.next; hops += 1
prev.next = None
print(f"singly + tail, delete last: {hops} hops")
print(f"removed: {tail.cargo}  new last: {prev.cargo}")

# doubly + tail: delete the last parcel
head = DBox(rows[0]["tracking"]); cur = head
for r in rows[1:]:
    b = DBox(r["tracking"]); cur.next = b; b.prev = cur; cur = b
tail = cur
pred = tail.prev
pred.next = None; tail.prev = None
print(f"doubly + tail, delete last: 0 hops")
print(f"removed: {tail.cargo}  new last: {pred.cargo}")
