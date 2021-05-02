class Stack:
    def __init__(self):
        self.array = []
    
    def peek(self):
        # See the last item
        if not self.array:
            return None
        return self.array[-1]
    
    def push(self, value):
        # Add the item to the top of the stack
        self.array.append(value)
        return self.array
    
    def pop(self):
        # Remove the last item
        return self.array.pop()
    
    def is_empty(self):
        # See whether a stack is empty
        return not bool(self.array)


if __name__ == "__main__":
    my_stack = Stack()
    print(f"Stack is empty: {my_stack.is_empty()}")
    my_stack.push(2)
    print(f"After push(2) stack is empty: {my_stack.is_empty()}")
    print(f"The last item in stack: {my_stack.peek()}")
    my_stack.push(True)
    print(f"The last item after push(True): {my_stack.peek()}")
    print(f"Popping the last item: {my_stack.pop()}")
    print(f"The last item in stack: {my_stack.peek()}")
