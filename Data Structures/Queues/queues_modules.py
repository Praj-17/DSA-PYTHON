from collections import deque

from sympy import Q

queue = deque()

# Left to Right
queue.appendleft(10)
queue.appendleft(20)
queue.appendleft(30)
queue.appendleft(40)
print(queue)
queue.pop()
queue.pop()
queue.pop()
print(queue)

from queue import Queue

#this method has a risk of getting blocked
# LEft to Right

#Use Put_nowait or get_nowait methods for proper functioning



queue = Queue()
queue.put(10)
queue.put(20)
queue.put(30)
print(queue.get())
print(queue.get())
print(queue.get())

