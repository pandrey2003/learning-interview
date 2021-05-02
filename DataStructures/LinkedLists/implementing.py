class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        if self.head:
            second_node = self.head
            self.head = new_node
            new_node.next = second_node
        else:
            self.head = new_node
    
    def shift(self):
        current_f_node = self.head
        needed_f_node = current_f_node.next
        self.head = needed_f_node
        del current_f_node
    
    def pop(self):
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
        
    
    def insert(self, index, data):
        new_node = Node(data)
        current = self.head
        # Just to finish at the previous node before replacing
        for _ in range(index-1):
            current = current.next
        before_node = current
        alt_node = current.next
        before_node.next = new_node
        new_node.next = alt_node
    
    def remove(self, index):
        current = self.head
        # Just to finish at the previous node before replacing
        for _ in range(index-1):
            current = current.next
        before_node = current
        after_node = current.next.next
        before_node.next = after_node
    
    def print_all_nodes(self):
        list_of_nodes = []
        current = self.head
        while current:
            list_of_nodes.append(str(current.data))
            current = current.next
        print(" -> ".join(list_of_nodes))


if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    print("appending 3")
    linked_list.append(3)
    linked_list.print_all_nodes()
    print("appending \'a\'")
    linked_list.append("a")
    linked_list.print_all_nodes()
    print("prepending True")
    linked_list.prepend(True)
    linked_list.print_all_nodes()
    print("Inserting \'at-index-a\' at index 2")
    linked_list.insert(2, "at-index-2")
    linked_list.print_all_nodes()
    print("appending 129")
    linked_list.append(129)
    linked_list.print_all_nodes()
    print("deleting the head")
    linked_list.shift()
    linked_list.print_all_nodes()
    print("deleting the end")
    linked_list.pop()
    linked_list.print_all_nodes()
    print("removing the element at index 1")
    linked_list.remove(1)
    linked_list.print_all_nodes()
