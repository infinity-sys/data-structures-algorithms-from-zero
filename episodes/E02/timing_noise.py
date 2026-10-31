import csv, random, time
rng = random.Random(1997)
rows = list(csv.DictReader(open("../../data/packages.csv")))
real = [r["tracking"] for r in rows]
box = ["DC" + "".join(rng.choices("0123456789", k=8)) for _ in range(600_000 - 600)] + real
target = box[-1]                         # the same search every time
for run in range(1, 6):
    t0 = time.perf_counter()
    steps = 0
    for x in box:
        steps += 1
        if x == target:
            break
    ms = (time.perf_counter() - t0) * 1e3
    print(f"run {run}: {ms:6.2f} ms   steps = {steps}")
