from structures import Chain, Node
letters = list("ABCD")
a = letters.copy(); shifts = 0
a.append(None)
for j in range(3,-1,-1):
    a[j+1] = a[j]; shifts += 1
    print("shift", letters[j], j, "to", j+1)
a[0] = "X"
print("front array:", " ".join(a), "shifts", shifts)
c = Chain(letters); c.head = Node("X",c.head)
print("front chain: X A B C D; hops 0; notes 2 (new.next and head)")
for n in (4,600):
    moves = 0
    for _ in range(n): moves += 1
    print("front on", n, "array shifts", moves, "chain notes", 2)
chain = Chain(range(600)); node = chain.head; hops = 0
for _ in range(300): node = node.next; hops += 1
print("index", node.value, "hops", hops)
node = chain.head; hops = 0
for _ in range(299): node = node.next; hops += 1
print("insert before index 300: predecessor",node.value,"hops",hops,"array shifts",600-300)
node = chain.head; hops = 0
while node.next is not chain.tail: node = node.next; hops += 1
print("delete last: predecessor",node.value,"hops",hops)
b = list("ABCD"); b.insert(2,"X")
print("middle after B:"," ".join(b),"array shifts",len(letters)-2,"chain notes",2)
s = []
for x in "ABC": s.append(x)
print("exercise check: push A B C; pop",s.pop(),"push X;",end=" "); s.append("X")
print("pop",s.pop(),"pop",s.pop(),"remaining"," ".join(s))
