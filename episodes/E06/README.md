# E06 — Recursion II: Tracing the Call Stack by Hand

Video: https://youtu.be/hJ93zqENm8o

Files in this folder:

- `mystery.py` — the riddle from the start of the episode: a tiny recursive
  function whose only visible output is what comes back. Run it:

  ```bash
  python3 mystery.py
  ```

  Prints `cba` for `mystery("abc")` — the function reverses a string — and
  `level` for `mystery("level")`, because a palindrome reversed is itself.
  The video traces every push and pop of this call on the call stack.

- `fact_trace.py` — factorial with tracing prints inside: watch the winding
  trip down (`fact(4)` → `fact(3)` → … → `fact(0)`) and the unwinding trip
  back up as each frame returns its value, ending with `fact(4) = 24`.
  The stack stays 5 frames deep at most — exactly as traced by hand in the
  video.

- `fib_calls.py` — Fibonacci with a real call counter. Prints the measured
  table from the video: `fib(5)` takes 15 calls, `fib(10)` takes 177,
  `fib(15)` takes 1,973, `fib(20)` takes 21,891, `fib(25)` takes 242,785,
  and `fib(30)` takes 2,692,537 calls — about ×11.1 more work for every +5
  added to `n`, while the computed value grows gently. Same code, wildly
  more work.

- `fib_tree.py` — draws the full recursion tree for `fib(4)`: 9 calls in
  total, with `fib(2)` computed 2 times, `fib(1)` 3 times, and `fib(0)`
  2 times — the repeated work the counter exposes, made visible.

This episode uses no dataset — everything is plain Python arithmetic.

Requires: Python 3.10+ (standard library only).
