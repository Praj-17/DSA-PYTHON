class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
def postorder(root: 'Node'):
    if not root:
        return
    ans = []
    def postorder(root):
        for i in root.children:
            postorder(i)
        ans.append(root.val)
    postorder(root)
    return ans