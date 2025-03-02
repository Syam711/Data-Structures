from heapq import heappop, heapify
def merge():
    n = int(input())
    heap = []
    for i in range(n):
        size = int(input())
        inp = list(map(int, input().split()))
        heap.extend(inp)
    
    return heap

heap = merge()
heapify(heap)
while heap:
    print(heappop(heap), end=' ')