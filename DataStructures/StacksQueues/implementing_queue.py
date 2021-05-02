class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    def peek(self):
        return self.first.value
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.last is None:
            self.first = self.last = new_node
            self.length += 1
            return self
        last_node = self.last
        last_node.next = new_node
        self.last = new_node
        self.length += 1
        return self
    
    def dequeue(self):
        if self.last is None:
            return None
        if self.length == 1:
            self.first = self.last = None
            self.length -= 1
            return None
        first_node = self.first
        self.first = first_node.next
        self.length -= 1
        return first_node
    
    def is_empty(self):
        return not bool(self.length)


if __name__ == "__main__":
    new_queue = Queue()
    print(new_queue.is_empty())
    print(new_queue.enqueue("abc"))
    print(new_queue.is_empty())
    print(new_queue.enqueue(245))
    print(new_queue.peek())
    print(new_queue.dequeue())
    print(new_queue.peek())
