import Balancer
from Node import Node


def add(current_node, value):
    if value <= current_node.value:
        if current_node.left is None:
            current_node.left = Node(value, current_node)
        else:
            add(current_node.left, value)
            current_node.left = Balancer.balance(current_node.left)
            current_node.left.parentNode = current_node
    else:
        if current_node.right is None:
            current_node.right = Node(value, current_node)
        else:
            add(current_node.right, value)
            current_node.right = Balancer.balance(current_node.right)
            current_node.right.parentNode = current_node
