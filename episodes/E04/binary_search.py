import csv, random
rows = list(csv.DictReader(open("../../data/packages.csv")))
real = sorted(r["tracking"] for r in rows)   # the sorted shelf
def looks(box, target):                      # binary search, counting looks
    steps, lo, hi = 0, 0, len(box) - 1
    while lo <= hi:
        steps += 1                           # one look at the middle
        mid = (lo + hi) // 2
        if box[mid] == target:
            return steps
        if box[mid] < target:
            lo = mid + 1                     # keep the right half
        else:
            hi = mid - 1                     # keep the left half
    return steps                             # absent: halved to the end
print("   rows  best  average  worst")
rng = random.Random(1997)                    # same seed as always
for n in (600, 60_000, 600_000):
    box = sorted(real + [f"DC{i:08d}" for i in range(n - 600)])
    best = looks(box, box[(n - 1) // 2])     # the very first middle
    sample = [looks(box, box[rng.randrange(n)]) for _ in range(2_000)]
    worst = looks(box, "DC99999999")         # a parcel that is not there
    print(f"{n:>7} {best:>5} {sum(sample)/len(sample):>8.1f} {worst:>6}")
