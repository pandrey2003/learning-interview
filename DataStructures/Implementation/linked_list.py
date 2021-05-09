from os import link


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, data):
        # O(1) with tail
        new_node = Node(data)
        self.length += 1
        if self.head is None:
            self.head = self.tail = new_node
            return
        former_tail = self.tail
        former_tail.next = new_node
        new_node.previous = former_tail
        self.tail = new_node

    def prepend(self, data):
        # O(1) with head
        new_node = Node(data)
        former_head = self.head
        new_node.next = former_head
        former_head.previous = new_node
        self.head = new_node
        self.length += 1

    def shift(self):
        # O(1) with head
        needed_head = self.head.next
        needed_head.previous = None
        self.head = needed_head
        self.length -= 1

    def pop(self):
        # O(1) with tail
        needed_tail = self.tail.previous
        needed_tail.next = None
        self.tail = needed_tail
        self.length -= 1

    def insert(self, index, data):
        if index > self.length:
            return "Index is bigger than LL length"
        if index == self.length:
            self.append(data)
            return
        if index == 0:
            self.prepend(data)
            return
        new_node = Node(data)
        # Code below is practically O(n/2) time comp.
        if index < (self.length-1)/2:
            parent_node = self.head
            # To stop right before the node to replace
            for _ in range(index-1):
                parent_node = parent_node.next
            successor_node = parent_node.next
        else:
            successor_node = self.tail
            # To stop right before the successor node
            for _ in range(index, self.length-1):
                successor_node = successor_node.previous
            parent_node = successor_node.previous
        parent_node.next = new_node
        new_node.previous = parent_node
        new_node.next = successor_node
        successor_node.previous = new_node
        self.length += 1

    def remove(self, index):
        if index > self.length:
            return "Index is bigger than LL length"
        if index == self.length:
            self.pop()
            return
        if index == 0:
            self.shift()
            return
        # Code below is practically O(n/2) time comp.
        if index < (self.length-1)/2:
            parent_node = self.head
            for _ in range(index-1):
                parent_node = parent_node.next
            replace_node = parent_node.next.next
        else:
            replace_node = self.tail
            for _ in range(index, self.length-2):
                replace_node = replace_node.previous
            parent_node = replace_node.previous.previous
        parent_node.next = replace_node
        replace_node.previous = parent_node
        self.length -= 1

    def print_all_nodes(self):
        if self.head is None:
            print("Linked list is empty")
            return
        node_values = []
        current_node = self.head
        while current_node:
            node_values.append(str(current_node.data))
            current_node = current_node.next
        print("->".join(node_values))

    def print_all_nodes_in_reverse(self):
        if self.head is None:
            print("Linked list is empty")
            return
        reverse_node_values = []
        current_node = self.tail
        while current_node:
            reverse_node_values.append(str(current_node.data))
            current_node = current_node.previous
        print("<-".join(reverse_node_values))


if __name__ == "__main__":
    linked_list = DoublyLinkedList()
    linked_list.append(6)
    linked_list.append(9)
    linked_list.append(13)
    linked_list.prepend(4)
    linked_list.prepend(2)
    linked_list.append(19)
    linked_list.print_all_nodes()
    linked_list.shift()
    linked_list.print_all_nodes()
    linked_list.pop()
    linked_list.print_all_nodes()
    linked_list.insert(1, "at_index_1")
    linked_list.print_all_nodes()
    linked_list.insert(4, "at_index_4")
    linked_list.print_all_nodes()
    linked_list.remove(4)
    linked_list.print_all_nodes()
    linked_list.remove(1)
    linked_list.print_all_nodes()
    linked_list.print_all_nodes_in_reverse()
