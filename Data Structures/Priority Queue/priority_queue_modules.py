from queue import PriorityQueue

pq = PriorityQueue()

pq.put_nowait(20)
pq.put_nowait(10)
pq.put_nowait(40)
pq.put_nowait(30)


#By Default The lowest number has the highest priority
print(pq.get_nowait())
print(pq.get_nowait())
print(pq.get_nowait())