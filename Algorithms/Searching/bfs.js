class Node {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class BinarySearchTree {
    constructor() {
        this.root = null;
    }
    insert(value) {
        let newNode = new Node(value);
        if (!this.root) {
            this.root = newNode;
            return this;
        }
        let currentNode = this.root;
        while (true) {
            if (value < currentNode.value && currentNode.left) {
                currentNode = currentNode.left;
                continue;
            }
            if (value < currentNode.value) {
                currentNode.left = newNode;
                return this;
            }
            if (currentNode.right) {
                currentNode = currentNode.right;
                continue;
            }
            currentNode.right = newNode;
            return this;
        }
    }
    breadthFirstSearch() {
        let currentNode = this.root;
        let list = [];
        let queue = [currentNode];
        while (queue.length > 0) {
             currentNode = queue.shift();
             list.push(currentNode.value);
             if (currentNode.left) {
                 queue.push(currentNode.left);
             }
             if (currentNode.right) {
                queue.push(currentNode.right);
            }
        }
        return list;
    }
}

function traverse(node) {
    const tree = { value: node.value };
    tree.left = node.left === null ? null : traverse(node.left);
    tree.right = node.right === null ? null : traverse(node.right);
    return tree;
}

const tree = new BinarySearchTree();
tree.insert(9);
tree.insert(4);
tree.insert(6);
tree.insert(20);
tree.insert(170);
tree.insert(15);
tree.insert(1);
console.log(JSON.stringify(traverse(tree.root)));
console.log(tree.breadthFirstSearch());
