from email import message
from platform import node


class Node:
    def __init__(self, data):
        self.data = data
        self.link = None
        
class CircularSinglyLinkedList():
    def __init__(self):
        self.head = None
    def traverse(self):
        if self.head is None:
            print("The Circular linked list is Empty")
        else:
            node = self.head
            while True:
                print(node.data, "-->", end = "")
                node = node.link
                if node == self.head:
                    break
            print("NULL")
            print("_____end___")
            
    def AddBegin(self,data):
              new_node = Node(data)
              new_node.link = self.head
              self.head = new_node
    def AddEnd(self,data):
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                return self.head
            else:
                cur = self.head
                while cur.link is not None:
                    cur = cur.link
                cur.link = new_node
    def AddBetweenNode(self,middle_node,data):
            """Adding a node after the middle node"""
            if middle_node is None:
                print("No middle node")
                return
            else:
                new_node = Node(data)
                new_node.link = middle_node.link
                middle_node.link = new_node
    def AddBetweenValue(self,value,data):
            """Adding a node after the middle node"""
            if self.head is None:
                print("No head node")
                return
            else:
                node = self.head 
                while node != None:
                    if node.data == value:
                        new_node = Node(data)
                        new_node.link = node.link
                        node.link = new_node
                        return
                    node = node.link
                print("Not Present")        
    def DeleteBeginNode(self):
        if self.head is None: 
            print("No head node")
        else:
            head  = self.head
            self.head = head.link
            head = None
    def DeleteLastNode(self):
        if self.head is None:
            print("No head node")
        else:
            node = self.head
            # print(node1.data)
            # print(node2.data)
            while node.link.link is not None:
                node = node.link
            node.link = None
            node = None
    def DeleteBetween(self, middle_node):
        '''Delete the node after middle'''
        if middle_node is None:
            print("middle node not found")
        else:
            to_delete = middle_node.link
            middle_node.link = to_delete.link
            to_delete = None
    def DeleteValue(self, value):
        '''Delete the first node with the given value'''
        if self.head is None:
            print('The list is Empty')
            return
        if self.head.data == value:
            self.DeleteBeginNode()
            return
        else:
            node = self.head
            while node is not None:
                if node.data == value:
                    break
                prev = node
                node = node.link
            if node == None:
                print("Value not found")
                return
            prev.link = node.link
            node = None
            
                       
        
    
        
        
        
            
            
                
                
            
            
            
      
ll1 =  CircularSinglyLinkedList()
ll1.traverse()
ll1.AddBegin(10)
# ll1.AddBegin(20)
# ll1.AddBegin(100)
# ll1.AddBegin(90)
# ll1.AddBegin(80)
# ll1.AddBegin(70)
# ll1.AddEnd(30)
# ll1.AddEnd(50)
# ll1.AddEnd(60)
# ll1.AddBetweenNode(ll1.head.link.link.link, 40)
# ll1.AddBetweenValue(50,200)
# ll1.AddBetweenValue(80,250)
# ll1.AddBetweenValue(80,250)
# ll1.AddBetweenValue(80,250)
# ll1.traverse()
# ll1.DeleteBeginNode()
# ll1.DeleteBeginNode()
# ll1.DeleteBeginNode()
# ll1.traverse()
# ll1.DeleteLastNode()
# ll1.DeleteLastNode()
# ll1.AddEnd(55)
# ll1.AddEnd(60)
# ll1.traverse()
# print(ll1.head.link.link.link.data)
# ll1.DeleteBetween(ll1.head.link.link.link)
# ll1.traverse()
# ll1.DeleteValue(250)
# ll1.traverse()
# ll1.DeleteValue(500)
# ll1.traverse()
# ll1.DeleteValue(250)
# ll1.DeleteValue(30)
# ll1.DeleteValue(55)
# ll1.traverse()