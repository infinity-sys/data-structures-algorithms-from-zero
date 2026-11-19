# E12 — Doubly Linked and Circular Lists

Video: https://youtu.be/T4FTFu0UzhI

Episode 12 of [Data Structures and Algorithms: From Zero to Hero](https://github.com/infinity-sys/data-structures-algorithms-from-zero).

## What you build
- `delete_last.py` — why a tail is not enough; 598 hops on 600 boxes (measured)
- `doubly.py` — `prev` note; delete-last in 0 hops; insert after with four notes
- `circular.py` — `last.next = head` on purpose; walk and length
- `doubly_circular.py` — both rings; forward and backward wraps
- `delete_last_delta.py` — same delete on 600 Delta Courier tracking numbers: 598 vs 0

## Run
```bash
python3 delete_last.py
python3 doubly.py
python3 circular.py
python3 doubly_circular.py
python3 delete_last_delta.py   # needs ../../data/packages.csv from the repo root
```

Python 3.13. Dataset: Delta Courier (fictional, seed 1997).
