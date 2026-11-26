# Load a Delta Courier van so the first delivery comes out first.
import csv
from stack import Stack

rows = list(csv.DictReader(open("../../data/packages.csv")))
route = [r for r in rows if r["origin"] == "Cairo" and r["status"] == "at hub"]
print("plan:  ", " ".join(r["destination"] for r in route))

van = Stack()
for r in reversed(route):           # last delivery goes in first
    van.push(r)
print("loaded", len(van), "| top:", van.peek()["tracking"], van.peek()["destination"])

stops = []
while not van.is_empty():
    stops.append(van.pop()["destination"])
print("unload:", " ".join(stops))
print("same as plan:", stops == [r["destination"] for r in route])
