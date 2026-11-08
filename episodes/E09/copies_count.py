import sys
def copies_for(n):
    a = []
    copies = 0
    prev = None
    for i in range(1, n + 1):
        a.append(i)
        s = sys.getsizeof(a)
        if s != prev and prev is not None:
            copies += i - 1            # move the i-1 residents
        prev = s
    return copies
print("      n   exact-fit   spare-wall   per append")
for n in (600, 60_000):
    exact = n * (n - 1) // 2           # rebuild on every append
    spare = copies_for(n)              # measured on real Python
    print(f"{n:>7,} {exact:>11,} {spare:>12,} {spare / n:>11.2f}")
print("per-append copies stay bounded: O(1)")
