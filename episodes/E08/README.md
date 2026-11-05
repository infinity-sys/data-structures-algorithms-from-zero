# E08 — Arrays and Python Lists: What Is Actually Inside

Video: https://youtu.be/DSxebyyWXAg

Files in this folder:

- `billion_looks.py` — the opening solution of the E07 exercise: a billion
  sorted parcels need only 30 looks. Run it:

  ```bash
  python3 billion_looks.py
  ```

  Prints `log2(n) = 29.9` and `looks = floor(log2(n)) + 1 = 30` — the closed
  form from episode 7, confirmed by the machine.

- `address_math.py` — a small model of array addressing: start byte 10,000,
  8-byte cells, `address(k) = start + k * cell`. Prints slots 0–3, slot 599
  (Delta's last van) and slot 999,999,999 — one multiply and one add for
  every position. That is O(1).

- `access_time.py` — the stopwatch proof. Builds a real list of
  10,000,000 slots, then reads the first, middle and last slot 5,000,000
  times each with `time.perf_counter()`. Prints the average nanoseconds
  per read — middle and last come out identical (measured: 12.8, 18.6,
  18.6 ns on a MacBook; your numbers will differ slightly, the equality
  will not).

- `references.py` — what a Python list really stores, weighed with
  `sys.getsizeof`: empty 56 bytes, one small int 64, two small ints 72,
  one huge 1,000-character label still 64. Slots hold 8-byte references;
  `id(a[0]) == id(a[1])` is `True` — arrows, not copies.

- `delta_slots.py` — jump versus scan on the fictional Delta Courier
  dataset (600 parcels, seed 1997): `slots[599]` reaches the last van in
  1 step; scanning from the top takes 600 looks.

  ```bash
  python3 delta_slots.py
  ```

Dataset: `delta_slots.py` reads `../../data/packages.csv` (the shared
Delta Courier dataset at the repo root, fictional, seed 1997), so run it
from inside this folder.

Requires: Python 3.10+ (standard library only).
