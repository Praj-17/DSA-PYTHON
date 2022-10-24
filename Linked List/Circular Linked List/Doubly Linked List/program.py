class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
    def traverse(self):
        if self.head is None:
            print("Empty List")
        else:
            cur = self.head
            while(True):
                print(cur.data, "<-->", end="")
                cur = cur.next
                if cur == self.head:
                    break
            print('__end__')
    def AddNode(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head
        new_node.prev = self.head#Condition to be circular
                #condition to be doubly circular
        
        if self.head is  None: #there is no element
            new_node.next = new_node   #Condition to be circular
            new_node.prev = new_node
        else:
            while(cur.next != self.head):
                cur = cur.next
            new_node.next = new_node.prev = new_node
        self.head = new_node

l1 = CircularDoublyLinkedList()
l1.traverse()
l1.AddNode(30)
l1.AddNode(40)
l1.AddNode(50)
l1.traverse()
print(l1.head.next.prev.data)
l1.traverse()


                
            
        
            
            
        