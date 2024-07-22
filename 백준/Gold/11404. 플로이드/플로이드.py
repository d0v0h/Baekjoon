import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

cost = [[1e9]*(n+1) for _ in range(n+1)]
# 자기 자신 방문 비용을 0으로 초기화
for x in range(1, n+1):
    for y in range(1, n+1):
        if x == y:
            cost[x][y] = 0

# a -> b로 가는 경로의 cost를 설정
for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a][b] = min(cost[a][b], c)

# 플로이드-워셜 
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            cost[a][b] = min(cost[a][b], cost[a][k] + cost[k][b])

# 각 노드에서 다른 노드로 방문하는 비용 출력
for arr in cost[1:]:
    for i in range(len(arr)):
        if arr[i] == 1e9:
            arr[i] = 0
    print(*arr[1:])