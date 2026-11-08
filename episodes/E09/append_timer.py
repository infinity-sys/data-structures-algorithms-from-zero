import time
N = 2_000_000
a = []
append = a.append
t0 = time.perf_counter()
for i in range(N):
    append(i)
total = time.perf_counter() - t0
print(f"appends: {N:,}")
print(f"total:   {total:.3f} s")
print(f"average: {total / N * 1e9:.1f} ns per append")
b = []
append = b.append
slowest = 0.0
for i in range(N):
    t0 = time.perf_counter()
    append(i)
    dt = time.perf_counter() - t0
    if dt > slowest:
        slowest = dt
print(f"slowest single append: {slowest * 1e9:,.0f} ns")
print("the occasional move, spread thin: O(1)")
