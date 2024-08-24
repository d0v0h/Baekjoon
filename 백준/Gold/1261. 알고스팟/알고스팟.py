import sys, heapq; input = sys.stdin.readline

n, m = map(int, input().split())

def dijkstra():
    queue = []
    heapq.heappush(queue, (graph[0][0], 0, 0))
    dist = [[1e9] * n for _ in range(m)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        cost, x, y = heapq.heappop(queue)
        cost = int(cost)

        if dist[x][y] < cost:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                next_cost = cost + int(graph[nx][ny])
                if dist[nx][ny] > next_cost:
                    dist[nx][ny] = next_cost
                    heapq.heappush(queue, (dist[nx][ny], nx, ny))
    return dist[m-1][n-1]

graph = []
for _ in range(m):
    route = list(input().strip())
    graph.append(route)

if n == 1 and m == 1:
    print(graph[0][0])
else:
    print(dijkstra())
