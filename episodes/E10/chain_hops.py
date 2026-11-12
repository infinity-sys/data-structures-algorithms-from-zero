class Box:
    def __init__(self, cargo):
        self.cargo = cargo
        self.next = None

head = None
for i in range(600, 0, -1):          # build: 600, 599, ..., 1
    b = Box(f"parcel {i}")
    b.next = head                    # each new box points forward
    head = b                         # head restarts the chain

print("the array answer: slots[599]      -> 1 step")
hops = 0
b = head
while b.cargo != "parcel 600":       # the last box built
    b = b.next                       # follow the note
    hops += 1
print(f"the chain answer: follow the notes -> {hops} hops")
print("walking replaces computing")
