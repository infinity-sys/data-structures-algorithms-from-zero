# Where should the top of a linked stack live? Count the work on 600 parcels.
import csv
from linked_stack import Node

rows = list(csv.DictReader(open("../../data/packages.csv")))
head = None
for r in reversed(rows):
    head = Node(r["tracking"], head)  # rows[0] ends up at the head

# top at the HEAD: pop = one link change, no walk
print("top at head: pop", head.value, "| hops 0")

# top at the TAIL: pop must find the node before the last
prev, hops = head, 0
while prev.next.next is not None:
    prev, hops = prev.next, hops + 1
print("top at tail: pop", prev.next.value, f"| hops {hops}")
