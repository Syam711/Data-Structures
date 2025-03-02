n = int(input())
arr = list(map(int, input().split()))
k = int(input())

dct = {}
for i in arr:
    if i not in dct: dct[i] = 1
    else: dct[i]+=1


count = 0
if k==0:
    for i in arr:
        dct[i] -= 1
        if i in dct and dct[i]>0:
            count += dct[i]
else:
    for i in arr:
        if i+k in dct and dct[i+k]>0:
            count += dct[i+k]

        
        
print(count)
        
# Sample Input 1

# 4
# 4 4 4 4 
# 0
# Sample Output 1

# 6