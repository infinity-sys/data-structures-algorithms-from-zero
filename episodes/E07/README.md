# E07 — Analyzing Recursive Algorithms: Recurrences, Gently

Video: https://youtu.be/Yzn7-znk98Y

Files in this folder:

- `fib6_check.py` — the opening solution of the E06 exercise: counts the
  calls for `fib(4)`, `fib(5)`, `fib(6)` with a real counter. Run it:

  ```bash
  python3 fib6_check.py
  ```

  Prints `calls(4) = 9`, `calls(5) = 15`, `calls(6) = 25`, then checks the
  recipe `calls(6) = calls(5) + calls(4) + 1` — `match: True`.

- `fact_steps.py` — factorial with a step counter: one tick per call.
  Prints 6, 11, 101, 501 steps for n = 5, 10, 100, 500 — exactly `n + 1`,
  the closed form of `T(n) = T(n−1) + 1`, `T(0) = 1`.

- `bsearch_steps.py` — binary search over n sorted parcel ids (the id at
  position `mid` is `mid`, so no array needs to be stored). Prints 4, 7,
  10, 20, 30 looks for n = 10, 100, 1,000, 1,000,000, 1,000,000,000 —
  exactly `floor(log2 n) + 1`, the closed form of `T(n) = T(n/2) + 1`.
  The 20 for a million is the same number episode 4 measured on the real
  dataset.

- `fib_identity.py` — the closed form of the Fibonacci call count,
  verified: for n = 5, 10, 15, 20, 25, 30 it prints the measured calls
  (15, 177, 1,973, 21,891, 242,785, 2,692,537) next to `2*fib(n+1) - 1`
  computed iteratively — `all rows match: True`.

- `growth_compare.py` — one table, three closed forms at the same n:
  factorial's `n + 1`, binary search's `floor(log2 n) + 1`, Fibonacci's
  `2*fib(n+1) - 1`. At n = 30: 31 steps vs 5 steps vs 2,692,537 calls.

This episode uses no dataset — everything is plain Python arithmetic.

Requires: Python 3.10+ (standard library only).
