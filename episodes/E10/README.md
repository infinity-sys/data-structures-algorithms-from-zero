# E10 — Linked Lists: Nodes and References

Video: https://youtu.be/D6FRNFruHrk

Files in this folder:

- `chain_hops.py` — the opening answer to the E09 exercise. Parcel 600 in an
  array: `slots[599]`, one computed step. In a chain of boxes: follow the
  notes from the head, 599 hops. Walking replaces computing — the word the
  array had and the chain gave up is *contiguity*. Run it:

  ```bash
  python3 chain_hops.py
  ```

- `boxes_ids.py` — three boxes (nodes) chained by hand, each holding a Delta
  parcel id as cargo. Prints their real memory ids: the boxes sit wherever
  the allocator put them — the arrows between them are 8-byte references,
  not copies. `a.next is b` prints `True`; the last note is `None`.
  (The printed ids vary run to run — that is the point: position does not
  matter, only the notes do. This run happened to land ~48 bytes apart —
  pure luck of the allocator, and the episode says so honestly.)

- `walk_count.py` — counts hops to reach the middle box (299), the last box
  (599), and to visit all 600 boxes (179,700 — the exact same total as E09's
  exact-fit wall rebuild; average 300 per visit, O(n)). The instant jump is
  gone; every position is paid for in walking.

- `grow_chain.py` — 600 arrivals, one at a time: 600 notes written, 0
  parcels moved. No moving days — remember episode 9's 24? A chain grows
  box by box and never rebuilds.

- `front_flip.py` — insert at the front: `before: 2 -> 3 -> 4`,
  `after: 1 -> 2 -> 3 -> 4`. Two notes written, zero moves — the surgery
  episode 11 prices in full.

All scripts are self-contained (no dataset needed). Memory ids differ on
every run; the hop counts and note counts do not.

Requires: Python 3.10+ (standard library only).
