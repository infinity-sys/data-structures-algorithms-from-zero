class Box:
    def __init__(self, cargo, next=None):
        self.cargo, self.next = cargo, next

def show(head):
    out, b = [], head
    while b is not None and len(out) < 8:    # stop at 8: a loop never ends
        out.append(b.cargo)
        b = b.next
    return " -> ".join(out) + (" ..." if b else "")

def insert_after(prev, cargo):
    new = Box(cargo)
    new.next = prev.next             # 1: new points at the old next
    prev.next = new                  # 2: prev points at new

head = Box("A", Box("B", Box("C", Box("D"))))
print("before:", show(head))
insert_after(head.next, "X")         # after B
print("after: ", show(head))

head = Box("A", Box("B", Box("C", Box("D"))))
b, new = head.next, Box("X")
b.next = new                         # WRONG ORDER: note 2 first...
new.next = b.next                    # ...so X points at itself
print("wrong: ", show(head))
