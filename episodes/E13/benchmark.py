"""Microseconds per workload. Setup and CSV loading excluded.
Pairs restore size. Seven samples per round, 200 workloads/sample, two rounds.
CPython built-ins versus a teaching Python chain: not equal implementation levels.
"""
import csv, json, platform
from pathlib import Path
from statistics import median
from time import perf_counter
from structures import Chain
HERE = Path(__file__).resolve().parent
paths = [HERE / "../../data/packages.csv", HERE / "../../../data/packages.csv"]
DATA = next(p.resolve() for p in paths if p.exists())
with DATA.open() as f:
    rows = list(csv.DictReader(f))
values = [r["tracking_id"] for r in rows] if "tracking_id" in rows[0] else [r[next(iter(r))] for r in rows]
N = len(values)
assert N == 600
B, REPEATS = 200, 7

def sample(setup, operation):
    objects = [setup() for _ in range(B)]
    t0 = perf_counter()
    for obj in objects:
        operation(obj)
    return (perf_counter() - t0) * 1e6 / B

def append_array(a):
    for v in values:
        a.append(v)

def append_chain(a):
    for v in values:
        a.append(v)

def front_array(a):
    a.insert(0, values[0]); a.pop(0)

def middle_array(a):
    a.insert(300, values[0]); a.pop(300)

def last_array(a):
    a.pop(); a.append(values[-1])

def known_chain(pair):
    a, pred = pair
    a.middle_pair(pred, values[0])

def known_setup():
    a = Chain(values)
    return a, a.at(299)

jobs = [
 ("append x600", list, append_array, Chain, append_chain),
 ("index 300", lambda:list(values), lambda a:a[300], lambda:Chain(values), lambda a:a.at(300).value),
 ("front insert+remove", lambda:list(values), front_array, lambda:Chain(values), lambda a:a.front_pair(values[0])),
 ("middle known insert+remove", lambda:list(values), middle_array, known_setup, known_chain),
 ("middle find+insert+remove", lambda:list(values), middle_array, lambda:Chain(values), lambda a:a.middle_pair(a.at(299), values[0])),
 ("last remove+append", lambda:list(values), last_array, lambda:Chain(values), lambda a:a.last_pair(values[-1])),
]
if __name__ == "__main__":
    print("Python", platform.python_version(), platform.python_implementation(), platform.system(), platform.machine())
    print("parcels", N, "samples", REPEATS, "batch", B, "unit microseconds/workload")
    result = {"python":platform.python_version(), "dataset":str(DATA), "n":N,"samples":REPEATS,"batch":B,"rounds":[]}
    for round_id in (1,2):
        print("ROUND", round_id)
        output = {}
        for label, sa, oa, sc, oc in jobs:
            sample(sa,oa); sample(sc,oc)
            aa, cc = [], []
            for r in range(REPEATS):
                for key in (("a","c") if r%2 == 0 else ("c","a")):
                    (aa if key == "a" else cc).append(sample(sa,oa) if key == "a" else sample(sc,oc))
            output[label] = {"array":aa,"chain":cc,"array_median":median(aa),"chain_median":median(cc)}
            print(f"{label}: array={median(aa):.3f} chain={median(cc):.3f}")
            print("  array samples", ", ".join(f"{x:.3f}" for x in aa))
            print("  chain samples", ", ".join(f"{x:.3f}" for x in cc))
        result["rounds"].append(output)
    (HERE/"measurements.json").write_text(json.dumps(result,indent=2))
