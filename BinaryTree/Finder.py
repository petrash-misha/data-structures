def find(value, current_node):
    if current_node is None:
        return None
    elif current_node.value is value:
        return current_node
    elif current_node.value < value:
        return find(value, current_node.right)
    else:
        return find(value, current_node.left)
