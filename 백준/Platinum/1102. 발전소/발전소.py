import sys; input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dp = [-1] * (1 << n)

visited = 0
cnt = 0
status = input().strip()
for i in range(len(status)):
    if status[i] == 'Y':
        visited |= (1 << i)     # 켜진 발전소 비트 마스킹
        cnt += 1

p = int(input())

def sol(visited, cnt):
    if cnt == p:
        return 0
    
    if dp[visited] != -1:
        return dp[visited]
    
    min_cost = 1e9
    for i in range(n):
        if visited & (1 << i):  # 켜져있는 발전소인 경우
            for j in range(n):
                if not visited & (1 << j):  # 꺼져있는 발전소 탐색
                    min_cost = min(min_cost, sol(visited | (1 << j), cnt+1) + graph[i][j])
    dp[visited] = min_cost
    return dp[visited]


if cnt >= p:
    print(0)
else:
    result = sol(visited, cnt)
    result = result if result != 1e9 else -1
    print(result)