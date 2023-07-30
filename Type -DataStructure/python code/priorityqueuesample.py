from queue import PriorityQueue
#thread-safe : 속도가 느림...
pq = PriorityQueue()
pq.put(6)
pq.put(10)
pq.put(13)
pq.put(-6)
pq.put(3)
while not pq.empty():
    print(pq.get()) #pop

#python 은 min-heap이라
#가장 낮은 값부터 순차적으로 queue에서 추출됨

#아래의 것이 위의 것보다 더 빠름!!
import heapq

pq = []
heapq.heappush(pq, 5)
heapq.heappush(pq, 12)
heapq.heappush(pq, 3)
heapq.heappush(pq, 0)
heapq.heappush(pq, -3)
heapq.heappush(pq, 2)
print(pq)
while pq:
    print(pq[0])
    heapq.heappop(pq)

#최상단에 가장 작은 값이 들어감!!! : python으로 작성할 때의 특징
