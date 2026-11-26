"""Teaching singly linked list with head and tail; standard library only."""
class Node:
    __slots__ = ("value", "next")
    def __init__(self, value, next=None):
        self.value, self.next = value, next

class Chain:
    def __init__(self, values=()):
        self.head = self.tail = None
        for value in values:
            self.append(value)

    def append(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def at(self, index):
        node = self.head
        for _ in range(index):
            node = node.next
        return node

    def front_pair(self, value):
        self.head = Node(value, self.head)
        self.head = self.head.next

    def middle_pair(self, pred, value):
        pred.next = Node(value, pred.next)
        pred.next = pred.next.next

    def last_pair(self, value):
        pred = self.head
        while pred.next is not self.tail:
            pred = pred.next
        pred.next = None
        self.tail = pred
        self.append(value)
