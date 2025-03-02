import heapq
from collections import deque

n = int(input())
people = list(map(int, input().split()))
k = int(input())

ind = deque([i for i in range(n)])
heap = [-i for i in people]
heapq.heapify(heap)
time = 0
while heap:
    if people[ind[0]]==-heap[0]:
        curr = ind.popleft()
        heapq.heappop(heap)
        time += 1
        if curr==k:
            break
    else:
        ind.append(ind.popleft())
        
print(time)