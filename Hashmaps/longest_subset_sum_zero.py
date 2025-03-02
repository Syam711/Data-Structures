n = int(input())
arr = list(map(int, input().split()))

curr_sum = max_len = 0
dct = {}

for i in range(n):
    curr_sum += arr[i]
    
    if curr_sum == 0:
        max_len = i+1
    
    if curr_sum in dct:
        max_len = max(max_len, i-dct[curr_sum])
    
    dct[curr_sum] = i
    
print(max_len)
