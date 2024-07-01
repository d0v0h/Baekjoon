import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

def bf():
    dist = [1e9] * (n+1)
    dist[1] = 0
    for i in range(n):
        for start, end, cost in graph:
            if dist[start] != 1e9 and dist[end] > dist[start] + cost:
                dist[end] = dist[start] + cost
                if i == n-1:
                    return -1
    return dist

result = bf()
if result == -1:
    print(-1)
else:
    for r in result[2:]:
        print(r if r != 1e9 else -1)