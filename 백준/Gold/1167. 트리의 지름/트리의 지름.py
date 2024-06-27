import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

v = int(input())
graph = [[] for _ in range(v+1)]

for _ in range(v):
    cmd = list(map(int, input().split()))[:-1]
    for i in range(1, len(cmd), 2):
        graph[cmd[0]].append((cmd[i], cmd[i+1]))

def DFS(node, distance):
    for next, next_dist in graph[node]:
        if visited[next] == -1:
            visited[next] = distance + next_dist
            DFS(next, distance + next_dist)

visited = [-1] * (v+1)
visited[1] = 0
DFS(1, 0)

last_node = visited.index(max(visited))
visited = [-1] * (v+1)
visited[last_node] = 0
DFS(last_node, 0)
print(max(visited))