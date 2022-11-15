def PreOrder(self): #root -> left -> right
            print(self.data, end = " ")
            if self.left:
                self.left.PreOrder()
            if self.right:
                 self.right.PreOrder()
