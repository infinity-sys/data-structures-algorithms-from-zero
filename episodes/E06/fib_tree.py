counts = {}

def fib(n, depth=0):
    counts[n] = counts.get(n, 0) + 1
    print("  " * depth + f"fib({n})")
    if n < 2:
        return n
    return fib(n - 1, depth + 1) + fib(n - 2, depth + 1)

fib(4)
total = sum(counts.values())
print(f"total calls: {total}")
for n in sorted(counts, reverse=True):
    if counts[n] > 1:
        print(f"fib({n}) ran {counts[n]} times")
