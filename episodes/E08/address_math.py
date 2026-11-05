START, CELL = 10_000, 8        # one model of byte addresses
def address(k):
    return START + k * CELL    # one multiply, one add
print("   slot     address")
for k in (0, 1, 2, 3):
    print(f"{k:>6} {address(k):>11,}")
print("   ...         ...")
print(f"{599:>6} {address(599):>11,}   <- last van slot")
print(f"{999_999_999:>6} {address(999_999_999):>11,}   <- a billionth")
print("one recipe, every slot: that is O(1)")
