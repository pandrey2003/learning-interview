class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0
    
    def peek(self):
        if self.first is None:
            return None
        return self.first.value

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = self.last = new_node
        else:
            former_last = self.last
            former_last.next = new_node
            self.last = new_node
        self.length += 1
        

    def dequeue(self):
        if self.first is None:
            return None
        if self.length == 1:
            self.first = self.last = None
        else:
            new_first = self.first.next
            self.first = new_first
        self.length -= 1

    def is_empty(self):
        return not bool(self.length)
