class Array:
    def __init__(self):
        self.length = 0
        self.data = {}
    
    def lookup(self, index):
        if index >= self.length:
            return f"No element at index {index}"
        return self.data[index]
    
    def append(self, value):
        self.data[self.length] = value
        self.length += 1
        return self.data
    
    def insert(self, index, value):
        if index > self.length:
            return "Index is bigger than array length"
        if index == self.length:
            self.append(value)
            return
        for lst_index in range(self.length-1, index-1, -1):
            moved_item = self.data[lst_index]
            self.data[lst_index+1] = moved_item
            del self.data[lst_index]
        self.data[index] = value
        self.length += 1

    def pop(self, index=None):
        if index is None:
            removed_item = self.data[self.length-1]
            del self.data[self.length-1]
            self.length -= 1
            return removed_item
        try:
            removed_item = self.data[index]
        except KeyError:
            return f"No element at index {index} in array"
        del self.data[index]
        self._del_at_index_next_elements_move_left(index)
        self.length -= 1
        return removed_item

    def remove(self, value):
        value_index = self._find_index_of_element(value)
        if value_index is None:
            return "Element not found"
        self._del_at_index_next_elements_move_left(value_index)
        self.length -= 1

    def _del_at_index_next_elements_move_left(self, index):
        for lst_index in range(index+1, self.length):
            moved_item = self.data[lst_index]
            self.data[lst_index-1] = moved_item
            del self.data[lst_index]
    
    def _find_index_of_element(self, element):
        for arr_index, arr_element in self.data.items():
            if arr_element == element:
                return arr_index



if __name__ == "__main__":
    my_array = Array()
    my_array.append("a")
    my_array.append("b")
    my_array.append("c")
    my_array.append("d")
    print("Appending \'e\':", my_array.append("e"), my_array.length)
    print("Lookup - catching error:", my_array.lookup(5))
    print("Lookup - index=3:", my_array.lookup(3))
    print("Popping - default:", my_array.pop())
    print("Popping - catching error:", my_array.pop(10))
    print("Object properties look like:", my_array.data, my_array.length)
    print("Popping from index=1:", my_array.pop(1))
    print("Object properties look like:", my_array.data, my_array.length)
    print("Inserting - catching error:", my_array.insert(10, "sth"))
    print("Inserting as append:", my_array.insert(3, "g"))
    print("Object properties look like:", my_array.data, my_array.length)
    print("Inserting at index=2:", my_array.insert(2, "first_insert"))
    print("Object properties look like:", my_array.data, my_array.length)
    print("Removing non-existent element:", my_array.remove("non-existent"))
    print("Removing \'first_insert\' element:", my_array.remove("first_insert"))
    print("Object properties look like:", my_array.data, my_array.length)
