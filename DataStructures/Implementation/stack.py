# Using array
class Stack:
    def __init__(self) -> None:
        self.array = []
    
    def peek(self):
        if not self.array:
            return None
        return self.array[-1]

    def push(self, value):
        self.array.append(value)
        return self.array

    def pop(self):
        returned_item = self.array.pop()
        return returned_item

    def is_empty(self):
        return not bool(self.array)
