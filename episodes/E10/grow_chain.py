class Box:
    def __init__(self, cargo):
        self.cargo = cargo
        self.next = None

head = None
flips = 0
moves = 0
for i in range(1, 601):
    b = Box(i)                       # any free corner
    b.next = head                    # write ONE note
    flips += 1
    head = b                         # head flips to the new box
print("600 arrivals, one at a time:")
print(f"  notes written: {flips}")
print(f"  parcels moved: {moves}")
print("no moving days — remember episode 9's 24?")
print("a chain grows box by box, never rebuilds")
