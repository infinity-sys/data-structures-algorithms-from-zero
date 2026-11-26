from structures import Chain
from benchmark import values, append_array, append_chain, front_array, middle_array, last_array

def items(a):
    out=[];node=a.head
    while node is not None:
        out.append(node.value);node=node.next
    assert a.tail is not None and a.tail.next is None
    assert a.tail.value==out[-1]
    return out
for op in (front_array,middle_array,last_array):
    a=list(values);op(a);assert a==values
for op in (lambda a:a.front_pair(values[0]),lambda a:a.middle_pair(a.at(299),values[0]),lambda a:a.last_pair(values[-1])):
    a=Chain(values);op(a);assert items(a)==values
x=[];append_array(x);assert x==values
x=Chain();append_chain(x);assert items(x)==values
assert Chain(values).at(300).value==values[300]
print('PASS: 600 unchanged tracking numbers; all edit pairs restore sequence and tail; both append builds and index agree.')
