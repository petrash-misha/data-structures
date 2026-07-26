import copy
from collections.abc import Callable
import math


class Node:
    key = None
    value = None

    def __init__(self, key, value):
        self.key = key
        self.value = value

def _to_int(data):
    return int.from_bytes(data.encode('utf-8'), byteorder='big')

class HashMap:
    _initial_size = 13
    _coefficient = 3
    _decrowding_coefficient = 0.25
    _crowding_coefficient = 0.75
    _count = 0
    _array = []


    def __init__(self):
        self.clear()
        self._prime = self.__get_largest_prime(len(self._array))

    def __get_largest_prime(self, limit: int) -> int:
        is_prime = [True] * (limit + 1)
        is_prime[0], is_prime[1] = False, False
        for i in range(2, int(math.sqrt(limit)) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False
        for i in range(limit, -1, -1):
            if is_prime[i]:
                return i


    def _h1(self, data):
        return _to_int(data) % len(self._array)

    def _h2(self, key):
        return self._prime - (_to_int(key) % self._prime)

    def add(self, key, value):
        if (self._count / len(self._array)) >= self._crowding_coefficient:
            self._re_hash(len(self._array) * self._coefficient)

        node = Node(key, value)
        self._add_node(node)
        self._count += 1

    def _add_node(self, node):
        hash1 = self._h1(node.key)
        hash2 = self._h2(node.key)
        index = hash1
        i = 1

        while self._array[index] != None:
            index = (hash1 + i * hash2) % len(self._array)
            i += 1

        self._array[index] = node


    def _re_hash(self, new_size):
        old_array = self._array
        self._array = [None] * new_size
        self._prime = self.__get_largest_prime(len(self._array))
        # print("PRIME: ", self._prime)
        for node in old_array:
            if node != None:
                self._add_node(node)

    def get(self, key):
        i = self._find(key)
        if i != None:
            return self._array[i].value
        return None


    def _find(self, key):
        hash1 = self._h1(key)
        hash2 = self._h2(key)
        index = hash1
        i = 1

        while self._array[index] != None:
            if self._array[index].key == key:
                return index
            index = (hash1 + i * hash2) % len(self._array)
            i += 1
        return None

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
