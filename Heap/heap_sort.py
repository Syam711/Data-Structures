def heapify(arr, i, n):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left<n and arr[left]>arr[largest]:
        largest = left
    if right<n and arr[right]>arr[largest]:
        largest = right

    if i!=largest:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest, n)
    
arr = list(map(int, input().split()))
for i in range(len(arr)//2-1, -1, -1):
    heapify(arr, i, len(arr))

for i in range(len(arr)-1, 0, -1):
    arr[0], arr[i] = arr[i], arr[0]
    heapify(arr, 0, i)

print(*arr)
