calls = 0

def fib(n):
    global calls
    calls += 1
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

counts = {}
for n in (4, 5, 6):
    calls = 0
    fib(n)
    counts[n] = calls

c4, c5, c6 = counts[4], counts[5], counts[6]
print(f"calls(4) = {c4}")
print(f"calls(5) = {c5}")
print(f"calls(6) = {c6}")
print()
print("recipe: calls(6) = calls(5) + calls(4) + 1")
print(f"                 = {c5} + {c4} + 1 = {c5 + c4 + 1}")
print(f"match: {c6 == c5 + c4 + 1}")
