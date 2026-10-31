import csv, random
rng = random.Random(1997)
rows = list(csv.DictReader(open("../../data/packages.csv")))
real = [r["tracking"] for r in rows]
def tracks(n):
    syn = ["DC" + "".join(rng.choices("0123456789", k=8)) for _ in range(n - 600)]
    return syn + real                    # real rows stay last
def find(box, target):                   # linear search, counting steps
    steps = 0
    for x in box:
        steps += 1                       # one comparison
        if x == target:
            return steps
    return steps
print("   rows  best  average   worst")
for n in (600, 60_000, 600_000):
    box = tracks(n)
    best, worst = find(box, box[0]), find(box, box[-1])
    avg = sum(find(box, t) for t in rng.sample(box, 200)) / 200
    print(f"{n:>7} {best:5d} {avg:8.1f} {worst:6d}")
