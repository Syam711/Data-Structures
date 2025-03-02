def heapify(arr, n, i):
    largest = i
    left = 2*i+1
    right = 2*i + 2

    if left<n and arr[left]>arr[largest]:
        largest = left
    
    if right<n and arr[right]>arr[largest]:
        largest = right
    
    if largest!=i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)

arr = []
for i in range(10):
    arr.append(i)
for i in range(4, -1, -1):
    heapify(arr, 10, i)

for i in range(9, 0, -1):
    arr[0], arr[i] = arr[i], arr[0]
    heapify(arr, i, 0)

print(arr)
