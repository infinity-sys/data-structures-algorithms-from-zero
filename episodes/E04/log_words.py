import math
print("          n   halvings = ceil(log2 n)")
for n in (10, 100, 1_000, 60_000, 600_000, 1_000_000, 1_000_000_000):
    print(f"{n:>11,}   {math.ceil(math.log2(n)):>3}")
