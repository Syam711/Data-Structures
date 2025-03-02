from heapq import heappop, heappush
class Klargest():
    def __init__(self, k, nums):
        self.k = k
        self.nums = []
        for i in nums:
            heappush(self.nums, i)
            if len(self.nums)>self.k:
                heappop(self.nums)
        
            
    def append(self, val):
        
        heappush(self.nums, val)
        if len(self.nums)>self.k:
            heappop(self.nums)
        
        return self.nums[0]

k = int(input())
size = int(input())
nums = list(map(int, input().split()))
heap = Klargest(k, nums)

n = int(input())
for _ in range(n):
    print(heap.append(int(input())), end=' ')
            