calls = 0

def fib(n):
    global calls
    calls += 1
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

def closed(n):
    """2*fib(n+1) - 1, computed iteratively."""
    a, b = 0, 1
    for _ in range(n + 1):
        a, b = b, a + b
    return 2 * a - 1

ok = True
for n in (5, 10, 15, 20, 25, 30):
    calls = 0
    fib(n)
    c = closed(n)
    ok = ok and (calls == c)
    print(f"n = {n:>2}   calls = {calls:>9,}   closed = {c:>9,}")

print()
print("closed(n) = 2*fib(n+1) - 1")
print(f"all rows match: {ok}")
