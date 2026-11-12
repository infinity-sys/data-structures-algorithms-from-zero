class Box:
    def __init__(self, cargo):
        self.cargo = cargo
        self.next = None

a = Box("DC85451018")
b = Box("DC85451019")
c = Box("DC85451020")
a.next = b
b.next = c

print("three boxes, anywhere in memory:")
for name, box in (("a", a), ("b", b), ("c", c)):
    print(f"  {name}: id {id(box):>13,}  cargo {box.cargo}")
print(f"a.next is b -> {a.next is b}")
print(f"b.next is c -> {b.next is c}")
print(f"c.next      -> {c.next}")
print("notes are references — 8-byte arrows, not copies")
