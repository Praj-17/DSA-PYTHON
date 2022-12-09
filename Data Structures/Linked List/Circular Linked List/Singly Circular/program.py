from email import message
from platform import node


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
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
                node = node.next
                if node == self.head:
                    break
            print("\n_____end___")
            
    def AddNode(self,data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head #circular linked list 
        if self.head is not None:
            while(cur.next != self.head):
                cur = cur.next
            cur.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node
    def DeleteNode(self):
        if self.head is None: 
            print("No head node")
        else:
            cur = self.head
            while(cur.next.next != self.head):
               cur = cur.next
            to_delete =cur.next
            cur.next = self.head
            to_delete = None
            
            
            
                       
        
    
        
        
        
            
            
                
                
            
            
            
      
ll1 =  CircularSinglyLinkedList()
ll1.traverse()
ll1.AddNode(10)
ll1.AddNode(20)
ll1.AddNode(30)
ll1.AddNode(40)
ll1.traverse()
ll1.DeleteNode()
ll1.DeleteNode()
ll1.traverse()
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