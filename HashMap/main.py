import copy
from collections.abc import Callable

class Node:
    key = None
    value = None

    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashMap:
    _initial_size = 10
    _coefficient = 3
    _decrowding_coefficient = 0.35
    _crowding_coefficient = 0.65
    _count = 0
    _array = []

    def __init__(self):
        self.clear()

    def _h(self, data, limit):
        return hash(data) % limit

    def add(self, key, value):
        if (self._count / len(self._array)) >= self._crowding_coefficient:
            self._re_hash(len(self._array) * self._coefficient)

        node = Node(key, value)
        self._add_node(node)
        self._count += 1

    def _add_node(self, node):
        i = self._h(node.key, len(self._array))

        while self._array[i] != None:
            i = self._h(node.key, len(self._array))
            if i == len(self._array):
                i = 0

        self._array[i] = node


    def _re_hash(self, new_size):
        old_array = self._array
        self._array = [None] * new_size
        for node in old_array:
            if node != None:
                self._add_node(node)

    def get(self, key):
        i = self._find(key)
        if i != None:
            return self._array[i].value
        return None

    def _find(self, key):
        i = self._h(key, len(self._array))
        ind = i
        node = self._array[i]
        while node == None or node.key != key:
            i += 1
            if ind == i:
                return None
            if i == len(self._array):
                i = 0
            node = self._array[i]
        return i

    def clear(self):
        self._array = [None] * self._initial_size
        self._count = 0

    def delete(self, key):
        i = self._find(key)
        if i == None:
            return None
        node = self._array[i]
        self._array[i] = None
        self._count -= 1

        new_size = len(self._array) // self._coefficient
        if new_size >= self._initial_size and self._count / new_size <= self._decrowding_coefficient:
            self._re_hash(new_size)

        return node.value

    def update(self, key, new_value):
        i = self._find(key)
        if i == None:
            return False
        self._array[i].value = new_value
        return True

    def each(self, func: Callable[[any, any], None]):
        for node in self._array:
            if node != None:
                func(node.key, node.value)

    def count(self):
        return self._count

    def copy(self):
        hashMap = HashMap()
        self.each(hashMap.add)
        return hashMap

    def deepcopy(self):
        hashMap = HashMap()
        self.each(lambda k, v: hashMap.add(copy.deepcopy(k), copy.deepcopy(v)))
        return hashMap
