import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

v = int(input())

graph = [[] for _ in range(v+1)]
for _ in range(v):
    cmd = list(map(int, input().split()))
    for i in range(1, len(cmd)-1, 2):
        graph[cmd[0]].append((cmd[i], cmd[i+1]))

def DFS(node, dist):
    for next_node, next_dist in graph[node]:
        if visited[next_node] == -1:
            visited[next_node] = next_dist + dist
            DFS(next_node, visited[next_node])

# 트리의 지름을 구하는 법
# 1. 비용이 가장 많이드는 노드 선택
# 2. 1의 노드를 시작점으로 비용이 많이드는 노드 선택
visited = [-1] * (v+1)
visited[1] = 0
DFS(1, 0)

large_length = -1
dest = -1
for i in range(1, v+1):
    if visited[i] > large_length:
        large_length = visited[i]
        dest = i

visited = [-1] * (v+1)
visited[dest] = 0
DFS(dest, 0)

print(max(visited))