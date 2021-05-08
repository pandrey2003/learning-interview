class HashTable:
    def __init__(self, size):
        self.data = [None] * size

    def _hash(self, key):
        hash = 0
        for i, element in enumerate(key):
            encoded_char = ord(element)
            hash = (hash + i * encoded_char) % len(self.data)
        return hash
    
    def set(self, key, value):
        address = self._hash(key)
        # print(f"Address for {key} is", address)
        if self.data[address] is None:
            self.data[address] = []
        self.data[address].append([key, value])
        return self.data[address]

    def get(self, key):
        address = self._hash(key)
        if self.data[address] is None:
            return "No such key in hash table"
        address_data = self.data[address]
        if len(address_data) == 1 and address_data[0][0] == key:
            # Ordinary case
            return address_data[0][1]
        # Below is because of hash collisions
        for data_lst in address_data:
            if data_lst[0] == key:
                return data_lst[1]
        return "No such key in hash table"

    def show_keys(self):
        addresses_with_data = [
            element
            for element in self.data
            if isinstance(element, list)
        ]
        if not addresses_with_data:
            return "Hash table is empty"
        keys_lst = []
        for element in addresses_with_data:
            if len(element) == 1:
                # Ordinary case
                keys_lst.append(element[0][0])
                continue
            for sub_element in element:
                # Hash collision
                keys_lst.append(sub_element[0])
        return keys_lst



if __name__ == "__main__":
    hash_table = HashTable(20)
    hash_table.set("oranges", 129)
    hash_table.set("bananas", 31)
    hash_table.set("apples", 98)
    print(hash_table.get("oranges"))
    print(hash_table.get("bananas"))
    print(hash_table.show_keys())

