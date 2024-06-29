import sys, heapq
input = sys.stdin.readline

n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, input().split())

def dijkstra(node):
    dist = [1e9] * (n+1)
    dist[node] = 0

    q = []
    heapq.heappush(q, (0, node))

    while q:
        cur_dist, cur_node = heapq.heappop(q)

        if dist[cur_node] < cur_dist:
            continue
        
        for next_dist, next_node in graph[cur_node]:
            total_dist = cur_dist + next_dist
            if dist[next_node] > total_dist:
                dist[next_node] = total_dist
                heapq.heappush(q, (total_dist, next_node))

    return dist

first_dist = dijkstra(1)
v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)

total_v1_path = first_dist[v1] + v1_dist[v2] + v2_dist[n]
total_v2_path = first_dist[v2] + v2_dist[v1] + v1_dist[n]

result = min(total_v1_path, total_v2_path)
print(result if result < 1e9 else -1)