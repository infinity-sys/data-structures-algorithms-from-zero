from stack import Stack

PAIRS = {")": "(", "]": "[", "}": "{"}

def check(text):
    s = Stack()
    for i, ch in enumerate(text):
        if ch in "([{":
            s.push(ch)
        elif ch in PAIRS:
            if s.is_empty():
                return f"closer {ch} at {i} has no opener"
            top = s.pop()
            if top != PAIRS[ch]:
                return f"mismatch at {i}: {top} closed by {ch}"
    if not s.is_empty():
        return f"{len(s)} opener(s) never closed"
    return "balanced"

for t in ["{[()]}", "([)]", "(()", "())", "rate[(w+2)*3]"]:
    print(f"{t:<14} {check(t)}")
