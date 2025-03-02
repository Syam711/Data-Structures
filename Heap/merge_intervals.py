from heapq import heappush, heappop
m = int(input())
n = int(input())

heap = []
for i in range(m):
    heappush(heap, tuple(map(int, input().split())))

prev_start, prev_end = heap[0][0], heap[0][1]

while heap:
    start, end = heappop(heap)
    if start<=prev_end:
        prev_end = end
        continue
    else:
        print(prev_start, prev_end)
        prev_start = start
        prev_end = end

print(prev_start, prev_end)

# Sample Input 1

# 4
# 2
# 1 3
# 2 6
# 8 10
# 15 18

# Sample Output 1

# 1 6
# 8 10
# 15 18