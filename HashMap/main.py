class Node:
    key = None
    value = None

    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashMap:
    array = [None] * 26

    def h(self,data, limit):
        return hash(data) % limit

    def add(self, key, value):
        node = Node(key, value)
        i = self.h(key, len(self.array))

        while self.array[i] != None:
            i += 1
            if i == len(self.array):
                i = 0


        self.array[i] = node

    def get(self, key):
        i = self.h(key, len(self.array))
        ind = i
        node = self.array[i]
        while node == None or node.key != key:
            i += 1
            if ind == i:
                return None
            if i == len(self.array):
                i = 0
            node = self.array[i]

        return node.value




    # def delete(self, key):
    #
    # def update(self, key, new_value):
    #
    # def each(self, func):
    #
    # def clear(self):
    #
    # def count(self):
    #
    # def clone(self):
    #
    # def deep_clone(self):




