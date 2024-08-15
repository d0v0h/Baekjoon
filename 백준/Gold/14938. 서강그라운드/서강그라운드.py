import sys, heapq
input = sys.stdin.readline

n, m, r = map(int, input().split())
item = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]

for i in range(r):
    a, b, l = map(int, input().split())
    graph[a].append([b, l])
    graph[b].append([a, l])

def dijkstra(node):
    dist = [1e9] * (n+1)
    dist[node] = 0

    queue = []
    heapq.heappush(queue, (0, node))

    while queue:
        cur_dist, cur_node = heapq.heappop(queue)

        if dist[cur_node] < cur_dist:
            continue

        for next_node, next_dist in graph[cur_node]:
            total_dist = cur_dist + next_dist
            if dist[next_node] > total_dist:
                dist[next_node] = total_dist
                heapq.heappush(queue, (total_dist, next_node))
            
    return dist

result = 0
for i in range(1, n):
    temp = 0
    dist = dijkstra(i)[1:]
    for i in range(len(dist)):
        if dist[i] <= m:
            temp += item[i]
    
    result = max(result, temp)

print(result)