class Box:
    def __init__(self, cargo, next=None):
        self.cargo, self.next = cargo, next

def chain(n):                        # head -> 1 -> 2 -> ... -> n, plus a tail
    head = None
    for i in range(n, 0, -1):
        head = Box(i, head)
    tail = head
    while tail.next is not None:
        tail = tail.next
    return head, tail

def walk_to(head, k):                # stand AT box k; count the hops
    b, hops = head, 0
    while b.cargo != k:
        b, hops = b.next, hops + 1
    return b, hops

rows = []
head, tail = chain(600)
head = Box("new", head)                                   # 2 notes
rows.append(("insert at the front", 0, 2))
head, tail = chain(600)
b, h = walk_to(head, 300)
b.next = Box("new", b.next)                               # 2 notes
rows.append(("insert after box 300", h, 2))
head, tail = chain(600)
tail.next = Box("new"); tail = tail.next                  # 2 notes
rows.append(("insert at the end (tail)", 0, 2))
head, tail = chain(600)
head = head.next                                          # 1 note
rows.append(("delete the front", 0, 1))
head, tail = chain(600)
b, h = walk_to(head, 299)                                 # stand BEFORE 300
b.next = b.next.next                                      # 1 note
rows.append(("delete box 300", h, 1))
head, tail = chain(600)
looks = [walk_to(head, k)[1] + 1 for k in range(1, 601)]
rows.append(("search, best", min(looks), 0))
rows.append(("search, average", sum(looks) / 600, 0))
rows.append(("search, worst", max(looks), 0))

print(f"{'operation (600 boxes)':<26}{'hops/looks':>11}{'notes':>7}")
for name, h, n in rows:
    print(f"{name:<26}{h:>11}{n:>7}")
