import csv, time, random
rng = random.Random(1997)
rows = list(csv.DictReader(open("../../data/packages.csv")))
real = [r["tracking"] for r in rows]
target = real[-1]                    # last row: worst case for a scan
def tracks(n):
    syn = ["DC" + "".join(rng.choices("0123456789", k=8)) for _ in range(n - 600)]
    return syn + real                # the real rows stay last
def timeit(box, inner=1, reps=300):
    best = 1e9
    for _ in range(reps):
        t0 = time.perf_counter()
        for _ in range(inner):
            target in box
        best = min(best, (time.perf_counter() - t0) / inner)
    return best * 1e6
print("rows  list_scan_us  set_lookup_us")
for n in (600, 60_000, 600_000):
    ts, st = tracks(n), set(tracks(n))
    print(f"{n:>7} {timeit(ts):12.1f} {timeit(st, inner=1000):12.3f}")
