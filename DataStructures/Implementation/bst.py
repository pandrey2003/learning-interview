class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        current_node = self.root
        while True:
            if value < current_node.value and current_node.left:
                # If value is less and there IS another Node below
                current_node = current_node.left
                continue
            if value > current_node.value and current_node.right:
                # If value is more and there IS another Node below
                current_node = current_node.right
                continue
            if value < current_node.value:
                # If value is less and we're on bottom of tree
                current_node.left = new_node
                break
            # If value is more and we're on bottom of tree
            current_node.right = new_node
            break

    def lookup(self, value):
        if self.root is None:
            return "No nodes in BST, lookup aborted"
        current_node = self.root
        i = 1
        while current_node:
            if value < current_node.value:
                current_node = current_node.left
                i += 1
                continue
            if value > current_node.value:
                current_node = current_node.right
                i += 1
                continue
            return f"Found item at #{i} level of BST"
        return "Not found"

    def remove(self, value):
        if self.root is None:
            return "BST is empty, operation aborted"
        # Finding the node and its parent
        current_node = self.root
        parent_node = None
        while current_node:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
                continue
            if value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
                continue
            ### Found the right node
            if not (current_node.left or current_node.right):
                # Case #1: node to be deleted is the leaf
                self._remove_node_leaf(parent_node, current_node)
            # Case #2: node has one child
            elif current_node.left and not current_node.right:
                # Case #2.1: node has left child, but not right
                self._remove_node_only_left_child(parent_node, current_node)
            elif current_node.right and not current_node.left:
                # Case #2.2: node has right child, but not left
                self._remove_node_only_right_child(parent_node, current_node)
            else:
                # Case #3: node has 2 children
                self._remove_node_two_children(parent_node, current_node)
            return

    @staticmethod  
    def _remove_node_leaf(parent_node: Node, current_node: Node):
        if current_node == parent_node.left:
            parent_node.left = None
            return
        parent_node.right = None
    
    @staticmethod
    def _remove_node_only_left_child(parent_node: Node, current_node: Node):
        if current_node == parent_node.left:
            parent_node.left = current_node.left
            return
        parent_node.right = current_node.left

    @staticmethod
    def _remove_node_only_right_child(parent_node: Node, current_node: Node):
        if current_node == parent_node.left:
            parent_node.left = current_node.right
            return
        parent_node.right = current_node.right
    
    @staticmethod
    def _remove_node_two_children(parent_node: Node, current_node: Node):
        if current_node.right.left:
            # Replacing node with in-order successor, if such exists
            inorder_successor = current_node.right.left
            if current_node == parent_node.left:
                parent_node.left = inorder_successor
            else:
                parent_node.right = inorder_successor
            inorder_successor.right = current_node.right
            inorder_successor.left = current_node.left
            inorder_successor.right.left = None
        elif current_node.left.right:
            # Replacing node with in-order predecessor
            inorder_predecessor = current_node.right.left
            if current_node == parent_node.left:
                parent_node.left = inorder_predecessor
            else:
                parent_node.right = inorder_predecessor
            inorder_predecessor.right = current_node.right
            inorder_predecessor.left = current_node.left
            inorder_predecessor.left.right = None
        elif current_node.right.right:
            # Unbalanced tree, according to AVL classification
            right_child = current_node.right
            if current_node == parent_node.left:
                parent_node.left = right_child
            else:
                parent_node.right = right_child
            right_child.left = current_node.left
            right_child.right = current_node.right.right
            right_child.right.right = None
        else:
            # Only left child has left child, right is without ones
            # OR neither of children has a child - the algorithm is the same
            right_child = current_node.right
            if current_node == parent_node.left:
                parent_node.left = right_child
            else:
                parent_node.right = right_child
            right_child.left = current_node.left
            right_child.right = current_node.right
            right_child.right = None


def printInorder(root):
    if root:
        # First recur on left child
        printInorder(root.left)
        # then print the data of node
        print(root.value),
        # now recur on right child
        printInorder(root.right)


def create_balanced_bst():
    my_bst = BinarySearchTree()
    my_bst.insert(20)
    my_bst.insert(10)
    my_bst.insert(30)
    my_bst.insert(5)
    my_bst.insert(17)
    my_bst.insert(23)
    my_bst.insert(39)
    my_bst.insert(1)
    my_bst.insert(6)
    my_bst.insert(12)
    my_bst.insert(19)
    my_bst.insert(22)
    my_bst.insert(28)
    my_bst.insert(35)
    my_bst.insert(58)
    return my_bst


if __name__ == "__main__":
    my_bst = create_balanced_bst()
    printInorder(my_bst.root)
    print(my_bst.lookup(20))
    print(my_bst.lookup(17))
    print(my_bst.lookup(58))
    my_bst.remove(58)
    my_bst.remove(1)
    my_bst.remove(5)
    my_bst.remove(39)
    printInorder(my_bst.root)
    print()
    ####
    new_bst = create_balanced_bst()
    printInorder(new_bst.root)
    print()
    new_bst.remove(1)
    new_bst.remove(5)
    new_bst.remove(12)
    new_bst.remove(10)
    new_bst.remove(30)
    printInorder(new_bst.root)
    ####
    new_bst = create_balanced_bst()
    print()
    new_bst.remove(6)
    new_bst.remove(12)
    new_bst.remove(19)
    new_bst.remove(10)
    printInorder(new_bst.root)
    ####
    new_bst = create_balanced_bst()
    print()
    new_bst.remove(6)
    new_bst.remove(12)
    new_bst.remove(19)
    new_bst.remove(1)
    new_bst.remove(10)
    printInorder(new_bst.root)
