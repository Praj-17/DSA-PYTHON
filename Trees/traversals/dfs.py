def bfs(root):
    if root is None:
        return
    queue = [root]
    traversal = []
    while len(queue) > 0:
        cur_node = queue.pop(0)

        if cur_node.left is not None:
            queue.append(cur_node.left)
            traversal.append(cur_node.left.data)

        if cur_node.right is not None:
            queue.append(cur_node.right)
            traversal.append(cur_node.right.data)
    return traversal