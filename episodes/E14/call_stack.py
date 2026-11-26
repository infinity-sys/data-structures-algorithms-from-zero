import sys

depth = 0


def total(n):
    global depth
    depth += 1
    print("  " * depth + f"push total({n})")
    result = 0 if n == 0 else n + total(n - 1)
    print("  " * depth + f"pop  total({n}) -> {result}")
    depth -= 1
    return result


print("answer", total(3))


def dive(n):
    return dive(n + 1) if n < 10**6 else n

try:
    dive(1)
except RecursionError:
    print("recursion limit", sys.getrecursionlimit(), "-> RecursionError")
