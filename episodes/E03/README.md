# E03 — Big-O Notation, Explained from Zero

Video: https://youtu.be/FU8LB81yvF0

Files in this folder:

- `count_pairs.py` — the pair counter from the episode: compares every
  pair exactly once at 600, 6,000 and 60,000 rows and prints the step
  count and the milliseconds. Run it:

  ```bash
  python3 count_pairs.py
  ```

  The step counts are exact — 179,700 then 17,997,000 then
  1,799,970,000 — and match the video to the digit. The milliseconds
  will not: timings depend on your machine. The 60,000-row run takes
  about half a minute (27,998.4 ms on the machine the video was
  recorded on). Do not try 600,000 rows: at that speed it would run
  for over an hour.

- `big_o_shapes.py` — the honesty table: the exact n(n−1)/2 count next
  to the n²/2 part we keep and the n/2 part we drop, with the dropped
  percentage (0.1669% at 600 rows, down to 0.0002% at 600,000). Pure
  arithmetic, no data file, instant — every digit matches the video.

`count_pairs.py` reads `../../data/packages.csv` (the shared Delta
Courier dataset at the repo root), so run it from inside this folder.

Requires: Python 3.10+ (standard library only).
