import sys
a = []
prev = None
jumps = []
for i in range(1, 601):
    a.append(i)
    s = sys.getsizeof(a)
    if s != prev:                      # the wall just grew
        jumps.append((i, s, (s - 56) // 8))
        prev = s
print(" append   new bytes   capacity")
for i, s, cap in jumps[:10]:
    print(f"{i:>7} {s:>11} {cap:>10}")
i, s, cap = jumps[-1]
print(f"   ... {len(jumps)} jumps over 600 appends")
print(f"final: {s:,} bytes, capacity {cap} for 600")
