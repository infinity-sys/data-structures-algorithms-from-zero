class DBox:
    def __init__(self, cargo):
        self.cargo = cargo
        self.next = None
        self.prev = None

def build_dc(labels):
    head = DBox(labels[0]); cur = head
    for c in labels[1:]:
        b = DBox(c); cur.next = b; b.prev = cur; cur = b
    cur.next = head; head.prev = cur     # close both ways
    return head, cur

def walk_fwd(head, n):
    out, b = [], head
    for _ in range(n):
        out.append(b.cargo); b = b.next
    return " -> ".join(out)

def walk_back(start, n):
    out, b = [], start
    for _ in range(n):
        out.append(b.cargo); b = b.prev
    return " -> ".join(out)

head, last = build_dc(["A", "B", "C", "D"])
print(f"last.next is head? {last.next is head}")
print(f"head.prev is last? {head.prev is last}")
print(f"forward 6:  {walk_fwd(head, 6)}")
print(f"backward 6: {walk_back(head, 6)}")
