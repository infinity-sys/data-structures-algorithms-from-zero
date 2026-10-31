def count(n):
    if n == 0:          # base case: answers directly
        print("Liftoff!")
        return
    print(n)            # a little work
    count(n - 1)        # recursive case: a smaller ask

count(5)
