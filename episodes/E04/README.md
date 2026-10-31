# E04 — Worst, Best and Average Case (and a Word About Logarithms)

Video: https://youtu.be/CocChulB-R8

Files in this folder:

- `binary_search.py` — the halving game from the episode: binary search
  that counts its looks, run at 600, 60,000 and 600,000 rows. For each
  size it prints the best case (the very first middle), the average over
  2,000 seeded random targets, and the worst case (a tracking id that is
  not there). Run it:

  ```bash
  python3 binary_search.py
  ```

  Every number matches the video to the digit — 1 / 8.3 / 10, then
  1 / 14.9 / 16, then 1 / 18.2 / 20 — because the random targets come
  from `random.Random(1997)`, the same seed as always. Note that the
  script sorts the ids first: halving only works on a sorted shelf.

- `log_words.py` — the counting-halves table: ⌈log₂ n⌉ for n = 10, 100,
  1,000, 60,000, 600,000, 1,000,000 and 1,000,000,000. Pure arithmetic,
  instant — 4, 7, 10, 16, 20, 20, 30, exactly as in the video.

`binary_search.py` reads `../../data/packages.csv` (the shared Delta
Courier dataset at the repo root), so run it from inside this folder.

Requires: Python 3.10+ (standard library only).
