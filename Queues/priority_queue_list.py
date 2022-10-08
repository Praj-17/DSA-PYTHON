#The difference between priorityQueue and normal queue is that.
# 1. In queue the first element according to the entry sequence is deleted 
# ex = Movie ticket line
# 2. But with priorityQueue the first element with the highest priority is deleted first
# ex = Hospital Line (critical patient Treated first)

pq = []
pq.append(20)
pq.append(10)
pq.append(40)
pq.append(30)
print(pq)
#considering the highest priority
pq.sort()
pq.pop()
pq.pop()
pq.pop()
print(pq)

#This is not the best method to implement Priority queue. As it takes a lot of time
