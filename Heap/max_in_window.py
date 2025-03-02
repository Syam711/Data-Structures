import heapq
n = int(input())
arr = list(map(int, input().split()))
k = int(input())
heap = []

for i in range(k-1):
    heapq.heappush(heap, (-arr[i], i))
for i in range(k-1, n):
    
    heapq.heappush(heap, (-arr[i], i))
    
    while heap[0][1]<=i-k:
        heapq.heappop(heap)
    
    print(-heap[0][0], end=' ')