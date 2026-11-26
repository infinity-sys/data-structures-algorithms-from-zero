# E14 — Stacks: Last In, First Out (Brackets, Undo, the Call Stack)

Video: https://youtu.be/FxU8Xffo4qA

Episode 14 of [Data Structures and Algorithms: From Zero to Hero](https://github.com/infinity-sys/data-structures-algorithms-from-zero).

## What you build
- `stack.py` — a stack on a Python list; the top is the END (append / pop, amortized O(1)).
- `linked_stack.py` — a stack on a singly linked chain; the top is the HEAD (2 notes, 0 hops per push).
- `undo_pile.py` — the E13 answer on both stacks: removed C X B, A is left.
- `stack_demo.py` — same behaviour from both representations; popping an empty stack raises IndexError (underflow).
- `brackets.py` — balanced-bracket check: push openers, pop and compare on closers, finish empty.
- `undo_redo.py` — undo and redo as two stacks, on a Delta Courier parcel status.
- `van.py` — load a Delta Courier van in reverse so it unloads in delivery order.
- `call_stack.py` — the call stack of `total(3)`, frame by frame, and the recursion limit.
- `top_cost.py` — where the top belongs on 600 parcels: head 0 hops, tail 598 hops per pop.

## Run
From this folder in the complete repository:
```bash
python3 undo_pile.py
python3 stack_demo.py
python3 brackets.py
python3 undo_redo.py
python3 van.py          # needs ../../data/packages.csv from the repo root
python3 call_stack.py
python3 top_cost.py     # needs ../../data/packages.csv
```
Standard library only. Recorded environment: Python 3.13.5, CPython, Linux x86_64. The output shown in the video is in `recorded_output.txt` (the recursion limit can differ on other systems).

Delta Courier is a fictional parcel company (600 parcels, seed 1997, dataset unchanged).

## Your turn (answer in E15)
Evaluate the postfix expression `5 1 2 + 4 * + 3 -` with a stack. A number is pushed; an operator pops twice (the second value popped is the left side), applies the operator and pushes the result. Write the stack after every token, the final value, and the most items the stack ever held. By hand first.
