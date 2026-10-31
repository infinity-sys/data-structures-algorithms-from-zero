# E01 — What Are Data Structures and Algorithms?

Video: https://youtu.be/zc1-jmmkC60

Files in this folder:

- `search_demo.py` — the timing experiment from the episode: scanning a
  Python list for one parcel id vs looking it up in a `set`, at 600,
  60,000 and 600,000 rows. Run it:

  ```bash
  python3 search_demo.py
  ```

  Your exact numbers will differ from the video (timings depend on the
  machine), but the pattern will be identical: the list scan grows
  linearly with the data, the set lookup stays flat.

- `peek.py` — the tiny pandas script from the episode: load
  `packages.csv`, print the shape, the first rows, and the
  `priority` value counts.

- `peek.ipynb` — the same three pandas steps as a Jupyter notebook, so
  you can run them cell by cell.

Both scripts read `../../data/packages.csv` (the shared Delta Courier
dataset at the repo root), so run them from inside this folder.

Requires: Python 3.10+ and pandas (`pip install pandas`).
