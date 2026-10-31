# E05 — Recursion I: Functions That Call Themselves

Video: https://youtu.be/0X_cL_aKzHM

Files in this folder:

- `countdown.py` — the first recursive function from the episode: count
  down from 5 and shout "Liftoff!". A base case (`n == 0`) that stops the
  calls, and a recursive case that moves one step toward it. Run it:

  ```bash
  python3 countdown.py
  ```

  Prints `5 4 3 2 1 Liftoff!`, exactly as in the video.

- `factorial.py` — recursion that returns a value: `n! = n × (n−1)!` with
  `0! = 1` as the base case. Prints the table from the video —
  `0! = 1`, `1! = 1`, `5! = 120`, `10! = 3,628,800` and the 20-digit
  `20! = 2,432,902,008,176,640,000`.

- `recursion_limit.py` — what happens when the base case is missing:
  Python's frame ceiling and the crash, measured for real. Prints
  `Python's frame ceiling: 1000` (from `sys.getrecursionlimit()`) and then
  shows that a runaway function dies with `RecursionError` after 999
  frames. This is the experiment behind the "999" tile in the video.

This episode uses no dataset — everything is plain Python arithmetic.

Requires: Python 3.10+ (standard library only).
