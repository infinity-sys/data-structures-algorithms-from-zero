# E11 — Linked List Operations by Hand: Insert, Delete, Search

Video: https://youtu.be/2ojl7wb6VGA

Files in this folder:

- `mid_insert.py` — the opening answer to the E10 exercise. Insert a new box
  after box 300 of a 600-box chain: finding the spot costs 299 hops from the
  head; the surgery itself changes 2 notes and moves 0 parcels
  (`300 -> new -> 301`). Run it:

  ```bash
  python3 mid_insert.py
  ```

- `insert_after.py` — insert X after B in `A -> B -> C -> D`. Wire the new
  note first (`X.next = B.next`), then cut (`B.next = X`):
  `A -> B -> X -> C -> D`. It also shows the wrong order — cut first, and X
  points at itself: `A -> B -> X -> X ...` (printing capped at 8 boxes).

- `delete_box.py` — delete by rewriting the note of the box BEFORE the
  target: delete C (1 hop, 1 note), delete the front A (0 hops, 1 note: move
  the head), delete a missing Z (walk to the end, 0 notes changed).

- `search_delta.py` — search the 600 real Delta Courier tracking numbers
  (`../../data/packages.csv`): first 1 look, middle 300, last 600, missing
  600. All 600 found: 180,300 looks, average 300.5 = (n + 1) / 2 — O(n).

- `tail_append.py` — append 600 parcels: with only a head, 179,101 hops in
  total; with one extra note (a tail pointer), 0 hops and 1,198 notes.

- `price_list.py` — the full price list for a 600-box chain: insert and
  delete at the ends are cheap, anything in the middle pays for the walk.

## Exercise (opens episode 12)

You have a chain of 600 boxes with a head AND a tail. Delete the LAST box.

1. The tail points right at it — so why is that not enough, and how many
   hops does it really take?
2. What one extra note per box would make it cheap?

Hint: the box BEFORE the target owns the note. The tail knows the last box —
but who knows the box before it?

The data file lives in `../../data/packages.csv` (Delta Courier is a
fictional company; the dataset is synthetic).

Requires: Python 3.10+ (standard library only). Measured with Python 3.13.
