import sys, heapq
input = sys.stdin.readline

v, e = map(int, input().split())

start = int(input())

graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

def dijkstra(node):
    distance = [1e9] * (v+1)
    distance[node] = 0

    q = []
    heapq.heappush(q, (0, node))

    while q:
        cur_dist, cur_node = heapq.heappop(q)

        if distance[cur_node] < cur_dist:
            continue

        for next_dist, next_node in graph[cur_node]:
            total_dist = cur_dist + next_dist
            if distance[next_node] > total_dist:
                distance[next_node] = total_dist
                heapq.heappush(q, (total_dist, next_node))
    
    return distance

dist = dijkstra(start)[1:]

for d in dist:
    print(d if d != 1e9 else 'INF')