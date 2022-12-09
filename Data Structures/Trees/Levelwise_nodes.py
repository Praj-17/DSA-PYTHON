def GetLevelWiseNodes(root):
    if not root:
        return []
        
    queue = [root]
    next_queue = []
    level = []
    result = []
    
    while queue:
        for root in queue:
            level.append(root.val)
            if root.left:
                next_queue.append(root.left)
            if root.right:
                next_queue.append(root.right)
        result.append(level)
        level = []
        queue = next_queue
        next_queue = []
    
    return result