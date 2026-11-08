import sys
print("        n  capacity   spare %")
for n in (100, 600, 10_000, 1_000_000):
    a = []
    append = a.append
    for i in range(n):
        append(i)
    cap = (sys.getsizeof(a) - 56) // 8
    print(f"{n:>9,} {cap:>9,} {100 * (cap - n) / n:>8.1f}")
print("spare stays near an eighth of n")
