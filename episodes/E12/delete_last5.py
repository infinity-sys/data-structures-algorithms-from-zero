class Box:
    def __init__(self, cargo, next=None):
        self.cargo, self.next = cargo, next

def show(head):
    out, b = [], head
    while b is not None:
        out.append(b.cargo); b = b.next
    return " -> ".join(out) if out else "(empty)"

head = Box("A", Box("B", Box("C", Box("D", Box("E")))))
tail = head
while tail.next is not None: tail = tail.next
print("before:", show(head), "  tail=", tail.cargo)
prev, hops = head, 0
while prev.next is not tail:
    prev = prev.next; hops += 1
print(f"walk to predecessor: {hops} hops → stand at {prev.cargo}")
prev.next = None
tail = prev
print(f"after:  {show(head)}  tail={tail.cargo}  ({hops} hops, 2 notes)")
