def fact(n):
    if n <= 1:              # base case
        return 1
    return n * fact(n - 1)  # recursive case

for n in (0, 1, 5, 10, 20):
    print(f"{n:>2}! = {fact(n):,}")
