print("   rows        exact = n(n-1)/2      n*n/2 part   n/2 part   dropped %")
for n in (600, 6_000, 60_000, 600_000):
    exact = n * (n - 1) // 2             # the real count
    big = n * n // 2                     # the part we keep
    small = n // 2                       # the part we drop
    pct = 100 * small / exact            # how little the dropped part is
    print(f"{n:>7} {exact:>20,} {big:>13,} {small:>10,} {pct:>10.4f}%")
