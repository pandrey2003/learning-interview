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
        return this.top;
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

const myStack = new Stack();
console.log(myStack.isEmpty());
myStack.push(2);
console.log(myStack.isEmpty());
console.log(myStack.peek());
myStack.push(true);
console.log(myStack.peek());
console.log(myStack.pop());
console.log(myStack.peek());
