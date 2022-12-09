queue = []

#enqueue

#Queue Right to left
queue.append(10)
queue.append(20)
queue.append(30)
print(queue)
queue.pop(0)
queue.pop(0)
print(queue)

#queue from left to right
queue.insert(0,10)
queue.insert(0,20)
queue.insert(0,30)
print(queue)
queue.pop()
queue.pop()
print(queue)
