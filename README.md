# Data Structures and Algorithms: From Zero to Hero

Code and datasets for every episode of the Infinity Systems YouTube course
**Data Structures and Algorithms: From Zero to Hero**.

The course starts from absolute zero — no programming or math background
assumed — and builds up to the data structures and algorithms every computer
science student is examined on: arrays, linked lists, stacks, queues, trees,
heaps, hash tables, graphs, sorting, searching, complexity analysis, and
algorithm design.

## Layout

- `data/` — the fictional **Delta Courier** dataset used across the whole
  course (`packages.csv`, `cities.csv`, `routes.csv`). It is generated
  (seed 1997) and completely fictional; any resemblance to real companies
  or cities' data is unintended.
- `episodes/E01/`, `episodes/E02/`, … — the exact code shown in each
  episode, one folder per episode, each with its own README linking the
  video.

## Running the code

You need Python 3.10+ and pandas:

```bash
pip install pandas
cd episodes/E01
python3 search_demo.py
python3 peek.py
```

Timing numbers you get will differ a little from the video — they depend on
your machine. The pattern (list scans grow linearly, set lookups stay flat)
will be the same.

## Videos

Each episode folder's README links its video. The full playlist link is in
the video descriptions.

---

Prepared by Infinity Systems.
