# Sample Input 1

# 7
# 3 7 2 1 9 8 41
# Sample Output 1

# 3
# Explanation 1

# Explanation: Sequence should be of consecutive numbers. Here we have 2 sequences with same length i.e. [1, 2, 3] and [7, 8, 9], but we should select [7, 8, 9] because the starting point of [7, 8, 9] comes first in input array and therefore, the output will be 7 9, as we have to print starting and ending element of the longest consecutive sequence.

n = int(input())
arr = list(map(int, input().split()))

dct = {}
for i in arr:
    dct[i] = dct.get(i, 0)
    
max_len = curr_len = 0
for i in dct.keys():
    tmp = i
    while i in dct and dct[i]!=-1:
        dct[i]-=1
        curr_len += 1
        i -= 1
    i = tmp
    while i+1 in dct and dct[i]!=-1:
        dct[i]-=1
        curr_len += 1
        i += 1
    max_len = max(max_len, curr_len)
    curr_len = 0
        
print(max_len)