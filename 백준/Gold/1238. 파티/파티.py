import sys, heapq
input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    route = list(map(int, input().split()))
    graph[route[0]].append((route[1], route[2]))

# 최단 경로 알고리즘 (heap으로 구현)
def dijkstra(node):
    dist = [1e9] * (n+1)
    dist[node] = 0

    q = []
    heapq.heappush(q, (node, 0))

    while q:
        # q에 들어있는 node와 이어지는 edge를 가져옴
        cur_node, cur_dist = heapq.heappop(q)

        # 현재 경로의 길이가 최단 길이인 경우
        if dist[cur_node] < cur_dist:
            continue

        else:
            for next_node, next_dist in graph[cur_node]:
                total_dist = cur_dist + next_dist
                if dist[next_node] > total_dist:
                    dist[next_node] = total_dist
                    heapq.heappush(q, (next_node, total_dist))

    return dist

x_to_home = dijkstra(x)[1:]

home_to_x = []
for i in range(1, n+1):
    home_to_x.append(dijkstra(i)[x])

result = [i+j for i, j in zip(home_to_x, x_to_home)]
print(max(result))