import heapq
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        arr[i] = -arr[i]
    heapq.heapify(arr)
    
    while True:
        if not arr: return 0
        
        if len(arr)==1: return -arr[0]
        
        if arr[0]==arr[1]:
            heapq.heappop(arr)
            heapq.heappop(arr)
        
        else:
            x = -heapq.heappop(arr)
            y = -heapq.heappop(arr)
            heapq.heappush(arr, y-x)
    
print(main())
        