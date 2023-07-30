from queue import PriorityQueue
#thread-safe : �ӵ��� ����...
pq = PriorityQueue()
pq.put(6)
pq.put(10)
pq.put(13)
pq.put(-6)
pq.put(3)
while not pq.empty():
    print(pq.get()) #pop

#python �� min-heap�̶�
#���� ���� ������ ���������� queue���� �����

#�Ʒ��� ���� ���� �ͺ��� �� ����!!
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

#�ֻ�ܿ� ���� ���� ���� ��!!! : python���� �ۼ��� ���� Ư¡
