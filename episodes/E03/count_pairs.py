import csv, time
rows = list(csv.DictReader(open("../../data/packages.csv")))
real = [r["tracking"] for r in rows]
def count_pairs(box):                    # compare every pair exactly once
    steps = 0
    n = len(box)
    for i in range(n):
        for j in range(i + 1, n):
            steps += 1                   # one comparison
    return steps
print("   rows        steps       ms")
for n in (600, 6_000, 60_000):
    box = real[:600] + [f"DC{i:08d}" for i in range(n - 600)]
    t0 = time.perf_counter()
    steps = count_pairs(box)
    ms = (time.perf_counter() - t0) * 1e3
    print(f"{n:>7} {steps:>12,} {ms:>8.1f}")
