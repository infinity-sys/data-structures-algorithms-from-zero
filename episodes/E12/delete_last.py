class Box:
    def __init__(self, cargo, next=None):
        self.cargo, self.next = cargo, next

def build(n):
    head = Box(0)
    cur = head
    for i in range(1, n):
        cur.next = Box(i)
        cur = cur.next
    return head, cur                     # head, tail

def delete_last(head, tail):
    # the box BEFORE the last owns the note — walk from the head
    if head is None:
        return None, None, 0, 0
    if head.next is None:                # one box: head moves
        return None, None, 0, 1
    prev, hops = head, 0
    while prev.next is not tail:
        prev = prev.next
        hops += 1
    prev.next = None                     # 1 note: skip the last box
    return head, prev, hops, 2           # +1 note: move the tail

head, tail = build(600)
print(f"chain: head={head.cargo}, tail={tail.cargo}, n=600")
head, tail, hops, notes = delete_last(head, tail)
print(f"delete last: {hops} hops, {notes} notes")
print(f"new tail cargo: {tail.cargo}")
print(f"why: predecessor is box {tail.cargo}; walk 0→{tail.cargo}")
