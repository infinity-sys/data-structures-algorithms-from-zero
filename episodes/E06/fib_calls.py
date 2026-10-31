calls = 0

def fib(n):
    global calls
    calls += 1
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

prev = None
for n in (5, 10, 15, 20, 25, 30):
    calls = 0
    r = fib(n)
    extra = f"   x{calls / prev:.1f}" if prev else ""
    print(f"fib({n:>2}) = {r:>8,}   calls = {calls:>10,}{extra}")
    prev = calls
