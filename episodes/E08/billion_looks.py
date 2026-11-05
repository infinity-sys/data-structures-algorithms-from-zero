import math
n = 1_000_000_000                      # a billion sorted parcels
print(f"n = {n:,} parcels, sorted")
print(f"log2(n) = {math.log2(n):.1f}")
looks = math.floor(math.log2(n)) + 1   # the E07 closed form
print(f"looks = floor(log2(n)) + 1 = {looks}")
print("a billion parcels, thirty looks")
print("IF the jump to any slot is instant")
