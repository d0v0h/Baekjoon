import sys
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# n개의 도시에 대해서 방문 최소값 저장
dp = [[-1] * (1 << n) for _ in range(n)]

def DFS(node, visited):
    if visited == (1 << n) - 1:
        if graph[node][0] != 0:
            return graph[node][0]
        else:
            return 1e9
    
    # 최소 경로를 이미 구한 경우
    if dp[node][visited] != -1:
        return dp[node][visited]
    
    min_cost = 1e9
    for i in range(1, n):
        # 다른 마을로 갈 수 없거나 방문한 경우 continue
        if graph[node][i] == 0 or visited & (1 << i):
            continue

        # DFS(i, visited | (1 << i))는 지금까지의 비용은 고려하지 않고 앞으로의 비용만 고려
        # ex) DFS(2, 0111) -> DFS(3, 1111) + graph[2][3] => 2에서 3으로가는 비용 + 3에서 0으로가는 비용
        #     DFS(1, 0011) -> DFS(2, 0111) + graph[1][2] => 위줄이 재귀형태로 호출되므로 1에서 2가는 비용 + (2에서 3가는 비용 + 3에서 0가는 비용)
        min_cost = min(min_cost, DFS(i, visited | (1 << i)) + graph[node][i])
        dp[node][visited] = min_cost
    return min_cost

print(DFS(0, 1))