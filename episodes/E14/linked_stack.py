class Node:
    def __init__(self, value, next=None):
        self.value, self.next = value, next

class LinkedStack:
    """Top = HEAD of a singly linked chain."""
    def __init__(self):
        self.head, self.size = None, 0

    def push(self, item):
        self.head = Node(item, self.head)
        self.size += 1

    def pop(self):
        if self.head is None:
            raise IndexError("pop from empty stack")
        node = self.head
        self.head = node.next
        self.size -= 1
        return node.value

    def peek(self):
        if self.head is None:
            raise IndexError("peek at empty stack")
        return self.head.value

    def is_empty(self):
        return self.head is None

    def __len__(self):
        return self.size
