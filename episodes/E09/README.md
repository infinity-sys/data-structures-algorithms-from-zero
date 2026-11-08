# E09 — Dynamic Arrays: How a Python list Grows (Amortized Cost)

Video: https://youtu.be/V5HZVwznWTY

Files in this folder:

- `wall_options.py` — the opening solution of the E08 exercise: parcel 601
  arrives at a full 600-slot wall. Exact fit leaves two options: refuse the
  parcel (0 moves, one lost parcel) or rebuild the whole wall — 600 moves
  today, 6,000 or 60,000 as the wall grows. One arrival should never cost a
  full move. Run it:

  ```bash
  python3 wall_options.py
  ```

- `grow_watch.py` — watch a real Python list grow, one append at a time,
  weighed with `sys.getsizeof` after each append. Prints the first ten
  "moving days" (appends 1, 5, 9, 17, 25, …), then the totals: 24 jumps
  over 600 appends, ending at 5,432 bytes = room for 672 parcels. The wall
  grows before it is full, and the jumps get rarer as it grows.

- `copies_count.py` — counts the exact item copies those moves cost, and
  compares with the simple bound "every move copies the current residents":
  at n = 600 the exact count is 179,700 while the moves themselves copied
  only 4,292 — 7.15 copies per append; at n = 60,000 it is 8.29 per append,
  settling toward ~9 (the growth factor ≈ 1.125, and f/(f−1) ≈ 9). A
  bounded price per append, no matter how big n gets.

- `append_timer.py` — the stopwatch proof. 2,000,000 appends timed with
  `time.perf_counter()`: 0.152 s total, 75.9 ns per append on average —
  and one slowest append of 3,414,583 ns (one moving day, ~45,000× the
  average, paid exactly once). That is amortized O(1) in one frame. Your
  numbers will differ; the pattern will not.

- `spare_fraction.py` — how much room the wall keeps spare: 100 → 108
  (8.0%), 600 → 672 (12.0%), 10,000 → 10,640 (6.4%),
  1,000,000 → 1,056,084 (5.6%). Spare stays near an eighth of n — the
  price of never rebuilding on every arrival.

All scripts are self-contained (no dataset needed). Timing and byte numbers
come from CPython 3 on a MacBook; rerun them anywhere — exact values shift,
the growth pattern does not.

Requires: Python 3.10+ (standard library only).
