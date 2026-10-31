import sys
print("Python's frame ceiling:", sys.getrecursionlimit())

depth = 0
def runaway():
    global depth
    depth += 1
    runaway()           # no base case, never smaller

try:
    runaway()
except RecursionError:
    print("RecursionError after", depth, "frames")
