
def Inorder(self): # left ->root-> right
        if self.left:
            self.left.Inorder()
        print(self.data, end = " ")
        if self.right:
                self.right.Inorder()