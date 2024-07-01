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
    prev_node = [0] * (n+1)

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
                # 최단 경로 갱신되면 이전 노드를 추가
                prev_node[next_node] = cur_node
                heapq.heappush(q, (total_dist, next_node))
    
    return dist, prev_node

cost, prev_node = dijkstra(start)
print(cost[end])
path = [end]
cur = end
while start != cur:
    cur = prev_node[cur]
    path.append(cur)
print(len(path))
for p in path[::-1]:
    print(p, end=' ')
