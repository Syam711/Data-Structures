import heapq
def shortestPath(edges, n, k):

    heap = [(0, k)]
    shortest = {i: float('inf') for i in range(1, n+1)}
    shortest[k] = 0

    while heap:
        curr_time, node = heapq.heappop(heap)

        if shortest[node]<curr_time:
            continue

        for neighbour, time in edges[node]:
            new_time = time + curr_time
            if new_time < shortest[neighbour]:
                shortest[neighbour] = time
                heapq.heappush(heap, (new_time, neighbour))

    max_time = max(shortest.values())
    return max_time if max_time!=float('inf') else 0

rows = int(input())
cols = int(input())

inp = [tuple(map(int, input().split())) for i in range(rows)]
n = int(input())
k = int(input())

edges = {i: [] for i in range(1, rows+1)}
for src, dest, time in inp:
    edges[src].append((dest, time))

print(shortestPath(edges, n, k))
