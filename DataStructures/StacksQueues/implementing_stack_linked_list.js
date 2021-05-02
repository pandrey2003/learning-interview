class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class Stack {
    constructor() {
        this.top = null;
        this.bottom = null;
        this.length = 0;
    }

    peek() {
        // see the last item
        return this.top;
    }

    push(value) {
        // add the item to the top of the stack
        let new_node = new Node(value);
        if (!this.length) {
            this.bottom = new_node;
        } else {
            new_node.next = this.top;
        }
        this.top = new_node;
        this.length++;
        return this.top;
    }

    pop() {
        // remove the last item
        if (!this.top) {
            return null;
        }
        if (this.top === this.bottom) {
            this.bottom = null;
        }
        let removedItem = this.top;
        this.top = this.top.next;
        this.length--;
        return removedItem;
    }

    isEmpty() {
        // see whether a stack is empty
        return !Boolean(this.length);
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
