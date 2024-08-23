import sys,heapq; input = sys.stdin.readline

def dijkstra(graph, n):
    queue = []
    # 비용, 시작지점
    heapq.heappush(queue, (graph[0][0], 0, 0))
    cost = [[1e9] * n for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        loss, x, y = heapq.heappop(queue)

        if cost[x][y] < loss:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                update_loss = loss + graph[nx][ny]

                if update_loss < cost[nx][ny]:
                    cost[nx][ny] = update_loss
                    heapq.heappush(queue, (update_loss, nx, ny))

    return cost[n-1][n-1]

n = int(input())
iter = 1

while n != 0:
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    
    print(f'Problem {iter}:', dijkstra(graph, n))

    n = int(input())
    iter += 1
