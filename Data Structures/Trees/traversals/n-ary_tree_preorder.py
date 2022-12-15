class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
def preorder(root: 'Node'):
    if not root:
        return
    ans = []
    def preorder(root):
        ans.append(root.val)
        for i in root.children:
            preorder(i)
        
    preorder(root)
    return ans