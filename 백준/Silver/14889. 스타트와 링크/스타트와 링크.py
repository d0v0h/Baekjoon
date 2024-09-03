import sys; input = sys.stdin.readline

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
visited = [False for _ in range(N)]

result = 0
MIN = int(1e9)
def btk(n, start):
    global MIN
    if n == N//2:
        start, link = 0, 0,

        for i in range(N):
            for j in range(N):
                if not visited[i] and not visited[j]:
                    link += graph[i][j]
                if visited[i] and visited[j]:
                    start += graph[i][j]
    
        MIN = min(MIN, abs(start - link))
        return

    for i in range(start, N):
        visited[i] = True
        btk(n+1, i+1)
        visited[i] = False

btk(0, 0)
print(MIN)