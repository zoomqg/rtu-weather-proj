class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity
        self.order = []

    def _hash(self, key):
        return hash(key) % self.capacity

    def _remove_oldest(self):
        if self.order:
            oldest_key = self.order.pop(0)
            self.remove(oldest_key)

    def insert(self, key, value):
        if key in self:
            self.remove(key)

        if self.size >= self.capacity:
            self._remove_oldest()

        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node

        self.order.append(key)
        self.size += 1

    def search(self, key):
        index = self._hash(key)

        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next

        raise KeyError(key)

    def remove(self, key):
        index = self._hash(key)

        previous = None
        current = self.table[index]

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                if key in self.order:
                    self.order.remove(key)
                return
            previous = current
            current = current.next

        raise KeyError(key)

    def __len__(self):
        return self.size

    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False

    def print_all(self):
        for index in range(self.capacity):
            current = self.table[index]
            while current:
                print(f"Date: {current.key}:\nResponse: {current.value}\n\n")
                current = current.next