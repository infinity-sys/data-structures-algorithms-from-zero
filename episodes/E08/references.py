import sys
empty = sys.getsizeof([])
one = sys.getsizeof([0])
two = sys.getsizeof([0, 0])
huge = sys.getsizeof(["DC" + "9" * 1000])
print(f"empty list       {empty:>4} bytes")
print(f"one small int    {one:>4} bytes")
print(f"two small ints   {two:>4} bytes")
print(f"one huge label   {huge:>4} bytes  <- same!")
a = [0, 0]
print("a slot holds a reference: 8 bytes")
print(f"id(a[0]) == id(a[1]): {id(a[0]) == id(a[1])}")
