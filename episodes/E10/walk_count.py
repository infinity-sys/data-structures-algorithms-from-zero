class Box:
    def __init__(self, cargo):
        self.cargo = cargo
        self.next = None
def hops_to(head, k):
    b, hops = head, 0
    while b.cargo != k:
        b = b.next
        hops += 1
    return hops
head = None
for i in range(600, 0, -1):
    b = Box(i)
    b.next = head
    head = b
print(f"middle {hops_to(head, 300)} hops")
print(f"last   {hops_to(head, 600)} hops")
total = sum(hops_to(head, k) for k in range(1, 601))
print(f"all    {total:,} hops — avg {total / 600:,.0f} — O(n)")
