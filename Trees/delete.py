def deleteNode(root, key):
  
    # Base Case
    if root is None:
        return root
  
    # If the key to be deleted 
    # is smaller than the root's
    # key then it lies in  left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)
  
    # If the kye to be delete 
    # is greater than the root's key
    # then it lies in right subtree
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
  
    # If key is same as root's key, then this is the node
    # to be deleted
    else:
  
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
  
        elif root.right is None:
            temp = root.left
            root = None
            return temp
  
        # Node with two children: 
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)
  
        # Copy the inorder successor's 
        # content to this node
        root.key = temp.key
  
        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)
  
    return root