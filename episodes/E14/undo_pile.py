# E13 answer: the undo pile, on both representations.
from stack import Stack
from linked_stack import LinkedStack

for S in (Stack, LinkedStack):
    s, removed = S(), []
    for x in "ABC":
        s.push(x)
    removed.append(s.pop())
    s.push("X")
    removed.append(s.pop())
    removed.append(s.pop())
    print(f"{S.__name__:<12} removed {' '.join(removed)} | left {s.peek()} | size {len(s)}")
