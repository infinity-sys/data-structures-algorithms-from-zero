# E13 — Array vs Linked List: Choosing with Real Timings

Video: https://youtu.be/1ANNABBSJgM

Episode 13 of [Data Structures and Algorithms: From Zero to Hero](https://github.com/infinity-sys/data-structures-algorithms-from-zero).

## What you build
- `structures.py` — teaching singly linked list with head and tail.
- `trace.py` — hand-trace confirmation: front shifts, index/middle/last hops, and the stack exercise answer (try it first).
- `benchmark.py` — two independent rounds, each with 7 batch means of 200 workloads; median in microseconds. Saves every sample to measurements.json.
- `test_correctness.py` — checks both append builds and that each edit pair restores the full sequence and tail.

## Run
From this folder in the complete repository:
```bash
python3 test_correctness.py
python3 trace.py
python3 benchmark.py
```
Uses `../../data/packages.csv` (the unchanged course data); no dependencies beyond the standard library.

Recorded environment: Python 3.13.5, CPython, Linux x86_64.

Delta Courier is fictional, with 600 parcels. Timings vary by system and load. The recorded timing compares native Python list methods with a teaching chain implemented in Python; it does not isolate hardware/cache/allocator effects. Setup, CSV reading, and printing are outside the timer. Append includes growth and node allocation. Edits are insert+remove pairs; last is remove+append. Known-predecessor and find+edit are separate workloads. Batch loop and call overhead remain in all measurements. Raw recording samples and output are included as recorded_measurements.json and recorded_output.txt; reruns write a separate measurements.json.

## Your turn (answer in E14)
Push A, B, C onto an empty pile; remove top; push X; remove top twice. Write removed order and remaining item. Choose the efficient top for a Python list and for a singly linked chain; name the operations and explain why.
