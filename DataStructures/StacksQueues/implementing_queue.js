class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class Queue {
    constructor() {
        this.first = null;
        this.last = null;
        this.length = 0;
    }
    peek() {
        return this.first;
    }
    enqueue(value) {
        let newNode = new Node(value);
        if (!this.last) {
            this.first = this.last = newNode;
            this.length++;
            return this;
        }
        let lastNode = this.last;
        lastNode.next = newNode;
        this.last = newNode;
        this.length++;
        return this;
    }
    dequeue() {
        if (!this.last) {
            return null;
        }
        if (this.length === 1) {
            this.first = this.last = null;
            this.length--;
            return null;
        }
        let firstNode = this.first;
        this.first = firstNode.next;
        this.length--;
        return firstNode;
    }
    isEmpty() {
        return !Boolean(this.length);
    }
}

if (require.main === module) {
    const newQueue = new Queue();
    console.log(newQueue.isEmpty());
    console.log(newQueue.enqueue("abc"));
    console.log(newQueue.isEmpty());
    console.log(newQueue.enqueue(245));
    console.log(newQueue.peek());
    console.log(newQueue.dequeue());
    console.log(newQueue.peek());
}
