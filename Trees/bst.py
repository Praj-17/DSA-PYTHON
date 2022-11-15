# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.right = None
#         self.left = None

import random as rand
class BST:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
    def Insert(self, data):
        if self.data is None:
            self.data = data
            return
        else:
            if data <= self.data:
                if self.left is not None:
                    self.left.Insert(data)
                else:
                    self.left = BST(data)
            else:
                if self.right is not None:
                    self.right.Insert(data)
                else:
                    self.right = BST(data)
    def Search(self,key):
        if self.data == key:
            print("Node is found")
            return self
        if key < self.data:
            if self.left:
                return self.left.Search(key)
            else:
                print("Node is not found")
                return
        else:
            if self.right:
                return self.right.Search(key)
            else:
                print("Node is not found")
                return
    def PreOrder(self): #root -> left -> right
            print(self.data, end = " ")
            if self.left:
                self.left.PreOrder()
            if self.right:
                 self.right.PreOrder()
    def PostOrder(self):  # left -> right->root
            if self.left:
                self.left.PostOrder()
            if self.right:
                 self.right.PostOrder()
            print(self.data, end = " ")
    def Inorder(self): # left ->root-> right
            if self.left:
                self.left.Inorder()
            print(self.data, end = " ")
            if self.right:
                 self.right.Inorder()
    def bfs(self):
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
    def Delete(self,key,root_data):
        if self.data is None :
            print("No data to delete")
            return self
        if key<self.data:
            if self.left:
                self.left = self.left.Delete(key, root_data)
            else:
                print("Given node is not Present")
        elif key>self.data:
            if self.right:
                self.right = self.right.Delete(key, root_data)
            else:
                print("Given node is not Present")
        else: 
            if self.left is None:
                temp = self.right
                if self.data == root_data:
                    self.key = temp.key
                    self.left = temp.left
                    self.right = temp.right
                    temp = None
                    return
                self = None
                return temp
            if self.right is None:
                temp = self.left
                if self.data == root_data:
                    self.key = temp.key
                    self.left = temp.left
                    self.right = temp.right
                    temp = None
                    return
                self = None
                return temp
            #else it has 2 child we will be replacing it with the immediate right child
            node = self.right
            while node.left:
                node = node.left
            self.data = node.data
            self.right = self.right.Delete(node.data, root_data)
        return self
    def MinValue(self):
        if self is None:
            return 
        cur = self
        while cur.left:
            cur = cur.left
        return cur.data 
    
    def MaxValue(self):
        if self is None:
            return 
        cur = self
        while cur.right:
            cur = cur.right
        return cur.data 
    def IsLeaf(self, key):
        cur = self.Search(key)
        if cur.left == cur.right == None:
            return True
        return False
    
            
    
def count(root):
    '''It returns the number of nodes within a tree'''
    if root is None:
        return 0
    return 1 + count(root.left) + count(root.right)
            
            
            
        
        
        
        
        
            
        
                 
            
root = BST(0)
l1 = [10, 5,16,2,18,4,13]
for i in l1:
    root.Insert(i)
root.Search(63)
print("Pre-order")
root.PreOrder()
print("\nIn-order")
root.Inorder()
print("\nPost-order")
root.PostOrder()
print(count(root))

root.Delete(5,10)


print(count(root))


print("Pre-order")
root.PreOrder()
print("\nIn-order")
root.Inorder()
print("\nPost-order")
root.PostOrder()

if count(root)>1:
    root.Delete(10,10)
else:
    print("Cannot perform delete by regular method ")

print("Pre-order")
root.PreOrder()
print("\nIn-order")
root.Inorder()
print("\nPost-order")
root.PostOrder()

print(root.MinValue())
print(root.MaxValue())

print(root.IsLeaf(13))
print(root.bfs())