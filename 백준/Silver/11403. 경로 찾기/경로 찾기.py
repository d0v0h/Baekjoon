import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def DFS(node):
    for i in range(n):
        if graph[node][i] == 1 and not visited[i]:  # node와 인접한 i를 찾음
            visited[i] = 1
            DFS(i)    # node와 인접한 i에 대해서 더 연결된 node를 찾음

for i in range(n):
    visited = [0 for _ in range(n)]    # i번째 노드와 연결된 다른 노드를 저장하기 위한 리스트
    DFS(i)
    print(*visited)