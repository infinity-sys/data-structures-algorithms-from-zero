import time
a = list(range(10_000_000))    # ten million real slots
REPS = 5_000_000
def ns_per(k):
    t0 = time.perf_counter()
    s = 0
    for _ in range(REPS):
        s += a[k]              # one indexed read
    return (time.perf_counter() - t0) / REPS * 1e9
print(f"list of {len(a):,} slots, {REPS:,} reads each")
print(" position   ns per read")
for name, k in (("first", 0), ("middle", 4_999_999),
                ("last", 9_999_999)):
    print(f"{name:>9} {ns_per(k):>12.1f}")
print("same cost everywhere: O(1) access")
