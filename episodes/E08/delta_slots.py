import csv
rows = list(csv.DictReader(open("../../data/packages.csv")))
slots = [r["tracking"] for r in rows]  # 600 slots
target = slots[-1]                     # the very last van
jump = slots[599]                      # way one: jump, 1 step
looks = 0
for t in slots:                        # way two: scan, counting
    looks += 1
    if t == target:
        break
print(f"parcels: {len(slots)}, want the last van")
print(f"jump to slot 599 -> {jump}")
print(f"   1 step, address computed")
print(f"scan from the top -> {looks} looks")
print("index arithmetic beats scanning")
