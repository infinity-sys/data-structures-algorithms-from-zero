def bsearch(n, x):
    # parcel ids are 0..n-1 in order, so the id at position mid is mid
    lo, hi = 0, n - 1
    steps = 0
    while lo <= hi:
        steps += 1
        mid = (lo + hi) // 2
        if mid == x:
            return steps
        if mid < x:
            lo = mid + 1      # keep the right half
        else:
            hi = mid - 1      # keep the left half
    return steps

for n in (10, 100, 1_000, 1_000_000, 1_000_000_000):
    print(f"parcels = {n:>13,}   steps = {bsearch(n, n - 1):>2}")
