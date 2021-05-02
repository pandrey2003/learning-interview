class Stack {
    constructor() {
        this.array = [];
    }

    peek() {
        // see the last item
        return this.array[this.array.length-1];
    }

    push(value) {
        // add the item to the top of the stack
        this.array.push(value);
        return this.array;
    }

    pop() {
        // remove the last item
        return this.array.pop();
    }

    isEmpty() {
        // see whether a stack is empty
        return !Boolean(this.array.length);
    }
}

if (require.main === module) {
    let myStack = new Stack();
    console.log("Stack is empty:", myStack.isEmpty());
    myStack.push(2);
    console.log("After push(2) stack is empty:", myStack.isEmpty());
    console.log("The last item in stack:", myStack.peek());
    myStack.push(true);
    console.log("The last item after push(true):", myStack.peek());
    console.log("Popping the last item:", myStack.pop());
    console.log("The last item in stack:", myStack.peek());
}
