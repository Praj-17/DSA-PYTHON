def PostOrder(self):  # left -> right->root
            if self.left:
                self.left.PostOrder()
            if self.right:
                 self.right.PostOrder()
            print(self.data, end = " ")