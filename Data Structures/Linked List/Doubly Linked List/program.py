from hashlib import new


class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList():
    def __init__(self):
        self.head = None
    def traverse(self):
        if self.head is None:
            print("head <--> Null")
            print("Empty list")
        else:
            node = self.head
            while node is not None:
                print(node.data, "<-->", end= "")
                node = node.next
            print(" Null")
            print("__end__")
    def AddBegin(self, data):
        head = self.head
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            head.prev = new_node
            new_node.next = head
            self.head = new_node
    def AddEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next =new_node
            new_node.prev = last
    def AddAfter(self,middle_node,data):
        new_node = Node(data)
        if middle_node is None:
            print("No middle node")
        else:
            if self.head.next is None:
                middle_node.next = new_node
                new_node.prev = middle_node
                return
            new_node.next = middle_node.next
            new_node.prev = middle_node
            middle_node.next = new_node
            new_node.next.prev = new_node
    def AddAfterValue(self, key,data):
        cur = self.head
        new_node = Node(data)
        if cur is None:
            print("The list is empty")
        while cur:
            if cur.data == key:
                if cur.next is None:
                    cur.next = new_node
                    new_node.prev = cur
                    return
                new_node.prev = cur
                new_node.next = cur.next
                cur.next.prev = new_node
                cur.next = new_node
                return
            cur = cur.next
            if cur is None:
                print("Value not in List")
                return
    def DeleteBegin(self):
        if self.head is None:
            print("The List is Empty")
        else:
            if self.head.next is None:
                self.head = None
                return
            self.head = self.head.next
            self.head.prev = None
    def DeleteEnd(self):
        if self.head is None:
            print("The List is Empty")
        else:
            to_delete = self.head
            while to_delete.next is not None:
                to_delete = to_delete.next
            if to_delete.prev is None:
                self.head= None
                return
            to_delete.prev.next = None
            to_delete = None
    def DeleteAfter(self, middle_node):
        if middle_node is  None:
            print("No middle node")
        else:
            to_delete = middle_node.next
            if middle_node.next is None:
                return
            to_delete.next.prev = middle_node
            middle_node.next = to_delete.next
            to_delete = None
    def DeleteAfterValue(self,value):
            if self.head is None:
                print("The list is empty")
                return
            else:
                node = self.head
                while node:
                    if node is None:
                        print("the value is not in list")
                        return
                    if node.data == value:
                        
                        if node.prev  == None or node.prev == node.next ==  None:
                    
                            return "No node after value node"
                        if node.next is None:
                            node.prev.next = None
                            node = None
                            return
                        node.prev.next = node.next
                        node.next.prev = node.prev
                        node = None
                        return
                    node = node.next
                    
            
        
        
                
                
                
                
        
            
    
            
        
     
l1 = DoublyLinkedList()
l1.AddEnd(3)
l1.AddBegin(4)
l1.AddBegin(5)
l1.AddBegin(6)
l1.AddBegin(7)
l1.AddBegin(15)
l1.AddBegin(16)
l1.AddEnd(9)
l1.traverse()
l1.AddAfter(l1.head, 10)
l1.AddAfterValue(10,11)
l1.AddAfterValue(200,11)
l1.traverse()
l1.DeleteBegin()
l1.traverse()
l1.DeleteEnd()
l1.traverse()
l1.DeleteEnd()
l1.traverse()
l1.DeleteAfter(l1.head.next)
l1.traverse()
l1.DeleteAfterValue(5)
l1.DeleteAfterValue(3)
l1.traverse()
