def exact_fit_moves(parcels):
    return parcels                     # move everyone to the new wall
print("parcel 601 arrives at a full wall")
print(" option 1: refuse        0 moves, one lost parcel")
for n in (600, 6_000, 60_000):
    print(f" option 2: rebuild {n:>6,} -> {n+1:>6,}"
          f"  moves: {exact_fit_moves(n):,}")
print("exact fit: one arrival costs a full move")
