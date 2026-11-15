class Box:
    def __init__(self, cargo):
        self.cargo = cargo
        self.next = None

head = None
for i in range(600, 0, -1):          # chain: parcel 1 -> ... -> parcel 600
    b = Box(i)
    b.next = head
    head = b

b, hops = head, 0                    # FIND box 300 (the "b" of the riddle)
while b.cargo != 300:
    b = b.next
    hops += 1
new = Box("new")                     # the SURGERY: two notes
new.next = b.next                    # note 1: new points at box 301
b.next = new                         # note 2: box 300 points at new
print(f"finding box 300: {hops} hops")
print("notes changed:   2 (new.next, then b.next)")
print("parcels moved:   0")
print(f"around the cut:  {b.cargo} -> {b.next.cargo} -> {b.next.next.cargo}")
