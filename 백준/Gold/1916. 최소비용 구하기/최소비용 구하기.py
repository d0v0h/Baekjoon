import sys, heapq
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

start, end = map(int, input().split())

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

print(dijkstra(start)[end])