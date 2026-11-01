steps = 0

def fact(n):
    global steps
    steps += 1          # one frame per call
    if n == 0:
        return 1
    return n * fact(n - 1)

for n in (5, 10, 100, 500):
    steps = 0
    fact(n)
    print(f"fact({n:>3})   steps = {steps:>4}   n + 1 = {n + 1:>4}")
