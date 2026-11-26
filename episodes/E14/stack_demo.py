from stack import Stack
from linked_stack import LinkedStack

for S in (Stack, LinkedStack):
    s = S()
    for parcel in ["P1", "P2", "P3"]:
        s.push(parcel)
    print(f"{S.__name__:<11} peek {s.peek()} pop {s.pop()} pop {s.pop()} size {len(s)}")
    s.pop()
    try:
        s.pop()
    except IndexError as e:
        print(f"{S.__name__:<11} empty {s.is_empty()}: IndexError")
