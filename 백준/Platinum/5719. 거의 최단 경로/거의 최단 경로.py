from collections import deque
import sys, heapq; input = sys.stdin.readline

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))

    dist = [float('inf')] * n
    dist[start] = 0

    while queue:
        cost, node = heapq.heappop(queue)

        if cost > dist[node]:
            continue

        for next_cost, next_node in graph[node]:
            total_cost = next_cost + cost
            if visited[node][next_node]:
                continue
            if total_cost < dist[next_node]:
                dist[next_node] = total_cost
                heapq.heappush(queue, (total_cost, next_node))
    
    return dist

def remove_short_path(end):
    queue = deque([end])
    while queue:
        node = queue.popleft()
        if node == s:
            continue

        for prev_cost, prev_node in graph_rev[node]:
            if dist[prev_node] + prev_cost == dist[node] and not visited[prev_node][node]:
                visited[prev_node][node] = True
                queue.append(prev_node)

if __name__ == '__main__':
    n, m = map(int, input().split())

    while n != 0 and m != 0:

        s, e = map(int, input().split())

        graph = [[] for _ in range(n)]
        graph_rev = [[] for _ in range(n)]      # 역방향 개념을 이용하여 최소 경로 간선 삭제

        for _ in range(m):
            a, b, c = map(int, input().split())
            graph[a].append((c, b))
            graph_rev[b].append((c, a))
        
        visited = [[False] * n for _ in range(n)]   # visited[n][m]에 대해 n -> m 방문 확인
        dist = dijkstra(s)

        if dist[e] == float('inf'):
            print(-1)
        else:
            remove_short_path(e)

            answer = dijkstra(s)
            
            if answer[e] == float('inf'):
                print(-1)
            else:
                print(answer[e])

        n, m = map(int, input().split())