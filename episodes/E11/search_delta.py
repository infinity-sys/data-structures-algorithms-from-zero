import csv

class Box:
    def __init__(self, cargo, next=None):
        self.cargo, self.next = cargo, next

rows = list(csv.DictReader(open("../../data/packages.csv")))
head = None
for r in reversed(rows):             # the chain keeps the file order
    head = Box(r["tracking"], head)

def search(head, key):
    b, looks = head, 0
    while b is not None:
        looks += 1                   # one comparison per box
        if b.cargo == key:
            return looks
        b = b.next
    return looks                     # missing: every box looked at

tests = {"first": rows[0]["tracking"], "middle": rows[299]["tracking"],
         "last": rows[-1]["tracking"], "missing": "DC00000000"}
for name, key in tests.items():
    print(f"{name:8}{key}  {search(head, key):>3} looks")
total = sum(search(head, r["tracking"]) for r in rows)
print(f"all 600 found: {total:,} looks, average {total / 600}")
