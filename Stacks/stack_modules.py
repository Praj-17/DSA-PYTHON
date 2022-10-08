from collections import deque
#Here Deque stands for double ended queue.
#But since we are implementing a stack we wont be using its other end. The function popleft and appendleft can do the needful
stack = deque(maxlen=5)
stack.append(6)
stack.append(5)
stack.append(5)
stack.append(5)
stack.append(5)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print(stack)


#This method is eneffiecient in poping beacuse it lags if you didnt handle empty funtion

from queue import LifoQueue

stack = LifoQueue(maxsize=5)
#Using put for push  and get for pop here

#Use Put_nowait or get_nowait methods for proper functioning
print(stack.put(5))
print(stack.put(6))
print(stack.put(7))
print(stack.put(8))
print(stack.get())
print(stack.get())
print(stack.get())
print(stack.get(timeout=1))
print(stack.get(timeout=1))
print(stack)

