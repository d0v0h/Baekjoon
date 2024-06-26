import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v+1)]

# 각 v별 다른 v방문 지점과 비용 저장
for _ in range(v-1):
    node_s, node_e, dist  = list(map(int, input().split()))
    graph[node_s].append((node_e, dist))
    graph[node_e].append((node_s, dist))

# DFS를 통해 각 노드까지의 누적 거리 계산
def DFS(node, dist):
    for n, n_dist in graph[node]:
        if visited[n] == -1:
            visited[n] = dist + n_dist
            DFS(n, visited[n])

# 트리 지름 1단계: 가장 멀리 떨어진 노드 계산
visited = [-1] * (v+1)
visited[1] = 0
DFS(1,0)

# 트리 지름 2단계: 가정 멀리 떨어진 노드에서 가장 먼 노드 계산
last_node = visited.index(max(visited))
visited = [-1] * (v+1)
visited[last_node] = 0
DFS(last_node, 0)
print(max(visited))