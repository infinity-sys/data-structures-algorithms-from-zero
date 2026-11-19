class Box:
    def __init__(self, cargo, next=None):
        self.cargo, self.next = cargo, next

def build_circular(labels):
    head = Box(labels[0])
    cur = head
    for c in labels[1:]:
        cur.next = Box(c); cur = cur.next
    cur.next = head                      # last.next = head — on purpose
    return head, cur

def walk(head, steps):
    out, b = [], head
    for _ in range(steps):
        out.append(b.cargo); b = b.next
    return " -> ".join(out)

def length(head):
    if head is None: return 0
    n, b = 1, head.next
    while b is not head:
        n += 1; b = b.next
    return n

head, last = build_circular(["A", "B", "C", "D"])
print(f"last.next is head? {last.next is head}")
print(f"walk 8 steps: {walk(head, 8)}")
print(f"length: {length(head)}")
