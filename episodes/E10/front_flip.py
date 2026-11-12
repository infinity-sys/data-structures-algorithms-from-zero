class Box:
    def __init__(self, cargo):
        self.cargo = cargo
        self.next = None

head = Box(2)
head.next = Box(3)
head.next.next = Box(4)

def show(head, label):
    out = []
    b = head
    while b is not None:
        out.append(str(b.cargo))
        b = b.next
    print(f"{label}: {' -> '.join(out)}")

show(head, "before")
new = Box(1)
new.next = head                      # note 1: the new box points at the old head
head = new                           # note 2: head restarts the chain
show(head, "after ")
print("insert at the front: 2 notes, 0 moves")
print("the surgery episode 11 prices in full")
