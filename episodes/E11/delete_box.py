class Box:
    def __init__(self, cargo, next=None):
        self.cargo, self.next = cargo, next

def show(head):
    out, b = [], head
    while b is not None:
        out.append(b.cargo)
        b = b.next
    return " -> ".join(out)

def delete(head, target):            # returns new head, hops, notes
    if head is not None and head.cargo == target:
        return head.next, 0, 1       # the head moves: 1 note
    prev, hops = head, 0
    while prev.next is not None and prev.next.cargo != target:
        prev, hops = prev.next, hops + 1
    if prev.next is None:
        return head, hops, 0         # not found: nothing changes
    prev.next = prev.next.next       # skip it: 1 note
    return head, hops, 1

head = Box("A", Box("B", Box("C", Box("D"))))
for t in ["C", "A", "Z"]:
    head, hops, notes = delete(head, t)
    print(f"delete {t}: {hops} hop(s), {notes} note(s)  ->  {show(head)}")
