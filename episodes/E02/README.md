# E02 — Counting Steps: How Fast Is Your Code, Really?

Video: https://youtu.be/TQC5xHbdmOU

Files in this folder:

- `count_steps.py` — the linear search that counts itself from the
  episode: searches the parcel ids at 600, 60,000 and 600,000 rows and
  prints the best, average and worst case in comparisons. Run it:

  ```bash
  python3 count_steps.py
  ```

  The script is seeded (`random.Random(1997)`), so your numbers should
  match the video exactly: best is always 1, average is about half of
  n, worst is exactly n.

- `timing_noise.py` — the clock experiment: the same worst-case search,
  five times in a row. The step count comes out identical every run
  (600,000), but the milliseconds never repeat — the point of the
  episode. Your timings will differ from the video; the count will not.

Both scripts read `../../data/packages.csv` (the shared Delta Courier
dataset at the repo root), so run them from inside this folder.

Requires: Python 3.10+ (standard library only).
