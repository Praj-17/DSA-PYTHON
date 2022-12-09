
import queue


queue = []

def isEmpty():
    if len(queue) == 0:
        return True
def Enqueue(element):
    queue.append(element)
def Dequeue():
    if IsEmpty():
        print ("Queue is empty")
    else:
        queue.pop(0)

queue.Enqueue(10)
queue.Enqueue(20)
queue.Enqueue(30)
queue.Enqueue(40)
print(queue)
queue.Dequeue()
queue.Dequeue()
print(queue)
    