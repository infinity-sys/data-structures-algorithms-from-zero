import math

def fib_fast(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(f"{'n':>4}   {'fact steps':>10}   {'search steps':>12}   {'fib calls':>12}")
for n in (10, 20, 30):
    a = n + 1
    b = math.floor(math.log2(n)) + 1
    c = 2 * fib_fast(n + 1) - 1
    print(f"{n:>4}   {a:>10,}   {b:>12,}   {c:>12,}")
