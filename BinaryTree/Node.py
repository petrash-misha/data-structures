class Node:
    def __init__(self, value, parentNode):
        self.value = value
        self.left = None
        self.right = None
        self.parentNode = parentNode

    def is_leaf(self):
        return self.left is None and self.right is None

    def is_two_children(self):
        return self.left is not None and self.right is not None

    def with_only_left(self):
        return self.left is not None and self.right is None

    def with_only_right(self):
        return self.right is not None and self.left is None

    def level(self):
        if self.parentNode is None:
            return 0

        return self.parentNode.level() + 1

    def print(self):
        print(self.value)
