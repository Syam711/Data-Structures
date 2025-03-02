from collections import deque
n = int(input())
arr = list(map(int, input().split()))
k = int(input())
queue = deque([])

for i in range(n):
    
    if queue and queue[0]<i-k+1:
        queue.popleft()
        
    while queue and arr[i]>arr[queue[-1]]:
        queue.pop()
    
    queue.append(i)
    
    if i>=k-1:
        print(arr[queue[0]], end=' ')