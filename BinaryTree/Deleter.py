import Balancer



def delete(node):
    if node is None:
        return False

    parent_node = node.parentNode
    # unexpected case as all nodes should have Parent except root node
    if parent_node is None:
        return False

    if node.is_leaf():
        _delete_leaf(node, parent_node)
    elif node.is_two_children():
        _delete_with_children(node, parent_node)
    elif node.with_only_left():
        _delete_with_left_child(node, parent_node)
    elif node.with_only_right():
        _delete_with_right_child(node, parent_node)
    else:
        raise "unexpected case one of above conditions should be true"

    # re-balancing

    balanced_node = None
    while parent_node is not None:
        grand_parent = parent_node.parentNode
        balanced_node = Balancer.balance(parent_node)
        if balanced_node is not parent_node:
            if grand_parent is not None:
                if parent_node == grand_parent.right:
                    grand_parent.right = balanced_node
                else:
                    grand_parent.left = balanced_node
                balanced_node.parentNode = grand_parent


        parent_node = balanced_node.parentNode

    return balanced_node

def _delete_leaf(node, parent_node):
    if parent_node.left is node:
        parent_node.left = None
    else:
        parent_node.right = None


def _delete_with_children(node, parent_node):
    rightest_node = _find_rightest(node.left)
    # we check the rightest_node is not direct child of node, as in that case below code works incorrectly
    if node.left != rightest_node:
        # Step  1: we move rightest_node.left child into rightest_node location
        rightest_node.parentNode.right = rightest_node.left
        if rightest_node.left is not None:
            rightest_node.left.parentNode = rightest_node.parentNode

        # Step 2: we replace node with rightest_node
        # Step 2.1: we move node children to rightest_node
        rightest_node.left = node.left
        node.left.parentNode = rightest_node

    rightest_node.right = node.right
    node.right.parentNode = rightest_node

    # Step 2.2: we finally associate rightest_node with parent_node, complete deletion node
    if parent_node.left == node:
        parent_node.left = rightest_node
    else:
        parent_node.right = rightest_node
    rightest_node.parentNode = parent_node


def _delete_with_left_child(node, parent_node):
    if parent_node.left == node:
        parent_node.left = node.left
    else:
        parent_node.right = node.left

    node.left.parentNode = parent_node


def _delete_with_right_child(node, parent_node):
    if parent_node.left == node:
        parent_node.left = node.right
    else:
        parent_node.right = node.right

    node.right.parentNode = parent_node


def _find_rightest(node):
    if node.right is None:
        return node
    else:
        return _find_rightest(node.right)


def delete_root(root):
    if root.is_leaf():
        return None
    elif root.with_only_left():
        return root.left
    elif root.with_only_right():
        return root.right
    elif root.is_two_children():
        rightest_node = _find_rightest(root.left)
        if rightest_node.parentNode != root:
            rightest_node.parentNode.right = rightest_node.left
            if rightest_node.left is not None:
                rightest_node.left.parentNode = rightest_node.parentNode

            rightest_node.left = root.left
            root.left.parentNode = rightest_node

        rightest_node.right = root.right
        root.right.parentNode = rightest_node

        return rightest_node
    else:
        raise "unexpected case one of above conditions should be true"
