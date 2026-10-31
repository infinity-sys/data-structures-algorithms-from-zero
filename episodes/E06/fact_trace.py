def fact(n, depth=0):
    print("  " * depth + f"-> call fact({n})")
    if n == 0:
        print("  " * depth + "<- returns 1")
        return 1
    r = n * fact(n - 1, depth + 1)
    print("  " * depth + f"<- returns {r}")
    return r

print("fact(4) =", fact(4))
