def dfs(current_node, action):
    if current_node is None:
        return
    else:
        dfs(current_node.left, action)
        action(current_node)
        dfs(current_node.right, action)

def bfs(node, action):
    queue = [node]
    while len(queue) != 0:
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
        action(node)