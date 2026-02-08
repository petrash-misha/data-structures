from Node import Node

SCREEN_WIDTH = 160

def call(node):
    if node is None:
        return

    nodes_in_line = []
    node_level = 0
    queue = [node]
    while len(queue) != 0:

        node = queue.pop(0)
        if node_level == node.level():
            nodes_in_line.append(node)
        else:
            _print_line(nodes_in_line)
            node_level += 1
            nodes_in_line = [node]

        # add next node into BFS queue
        if node.value is not None:
            if node.left is None:
                queue.append(Node(None, node))
            else:
                queue.append(node.left)
            if node.right is None:
                queue.append(Node(None, node))
            else:
                queue.append(node.right)

    # print last line
    _print_line(nodes_in_line)

def _print_line(array):
    node_level = 0
    for node in array:
        if node is not None:
            node_level = node.level()
            break
    p = int(SCREEN_WIDTH // (2 ** node_level))
    o = int(p // 2)
    line = o * ' '
    for node in array:
        if node.value is not None:
            parent = node.parentNode
            if parent is None:
                parent_val = '#'
            else:
                parent_val = str(parent.value)

            node_text = str(node.value) + '(' + parent_val + ')'
        else:
            node_text = ' @ '

        line += node_text + (p - len(node_text)//2) * ' '

    print(line)
    print(' ')

