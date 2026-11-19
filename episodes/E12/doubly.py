class DBox:
    def __init__(self, cargo):
        self.cargo = cargo
        self.next = None
        self.prev = None                 # the extra note: points backwards

def show(head):
    out, b, n = [], head, 0
    while b is not None and n < 12:
        out.append(str(b.cargo)); b = b.next; n += 1
    return " <-> ".join(out)

def build(labels):
    head = DBox(labels[0])
    cur = head
    for c in labels[1:]:
        b = DBox(c)
        cur.next = b; b.prev = cur
        cur = b
    return head, cur

def delete_last(head, tail):
    # tail.prev is the predecessor — 0 hops
    hops, notes = 0, 0
    if tail is None:
        return None, None, 0, 0
    pred = tail.prev
    if pred is None:                     # only one box
        return None, None, 0, 1
    pred.next = None; notes += 1         # cut forward note
    tail.prev = None; notes += 1         # clear backward note
    return head, pred, hops, notes + 1   # +1: move the tail

def insert_after(prev, cargo):
    # insert X after prev: 4 notes (next+prev both ways)
    x = DBox(cargo)
    nxt = prev.next
    x.next = nxt; x.prev = prev          # wire the new box
    prev.next = x
    if nxt is not None:
        nxt.prev = x
    return x

head, tail = build(["A", "B", "C", "D"])
print("before:", show(head), "  tail=", tail.cargo)
head, tail, hops, notes = delete_last(head, tail)
print(f"delete last D: {hops} hops, {notes} notes  ->  {show(head)}  tail={tail.cargo}")
x = insert_after(head.next, "X")         # after B
print(f"insert X after B: {show(head)}")
