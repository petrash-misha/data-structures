import Adder
import Balancer
import Deleter
import Finder
import Printer
from Node import Node


class BinaryTree:
    def __init__(self):
        self.root = None

    def print(self):
        Printer.call(self.root)

    def add(self, value):
        if self.root is None:
            self.root = Node(value, None)
        else:
            Adder.add(self.root, value)
            self.root = Balancer.balance(self.root)
            self.root.parentNode = None

    def delete(self, value):
        delete_node = Finder.find(value, self.root)
        if delete_node == self.root:
            self.root = Balancer.balance(Deleter.delete_root(self.root))
            if self.root is not None:
                self.root.parentNode = None
        else:
            self.root = Deleter.delete(delete_node)

    def update(self, old, new):
        if self.delete(old):
            self.add(new)
            return True
        return False

    def find(self, value):
        return Finder.find(value, self.root)


