def balance(node):
    if node is None:
        return None
    left_depth = _tree_height(node.left)
    right_depth = _tree_height(node.right)
    difference = abs(left_depth - right_depth)
    if difference < 2:
        return node

    if left_depth > right_depth:
        if node.left.right is None:
            return _ll_rotation(node)
        else:
            return _lr_rotation(node)

    else:
        if node.right.left is None:
            return _rr_rotation(node)
        else:
            return _rl_rotation(node)

def _tree_height(node):
    if node is None:
        return 0

    left_height = _tree_height(node.left)
    right_height = _tree_height(node.right)
    return max(left_height, right_height) + 1

def _ll_rotation(node):
        left = node.left
        parent = node.parentNode

        node.left = left.right
        if left.right:
            left.right.parentNode = node

        left.right = node
        node.parentNode = left

        left.parentNode = parent
        if parent:
            if parent.left == node:
                parent.left = left
            else:
                parent.right = left

        return left


def _rr_rotation(node):
        right = node.right
        parent = node.parentNode

        node.right = right.left
        if right.left:
            right.left.parentNode = node

        right.left = node
        node.parentNode = right

        right.parentNode = parent
        if parent:
            if parent.left == node:
                parent.left = right
            else:
                parent.right = right

        return right


def _lr_rotation(node):
    l_node = node.left
    node.left = l_node.right
    l_node.right = None
    node.left.left = l_node
    node.left.parentNode = node
    l_node.parentNode = node.left
    return _ll_rotation(node)

def _rl_rotation(node):
    r_node = node.right
    node.right = r_node.left
    r_node.left = None
    node.right.right = r_node
    node.right.parentNode = node
    r_node.parentNode = node.right
    return _rr_rotation(node)
