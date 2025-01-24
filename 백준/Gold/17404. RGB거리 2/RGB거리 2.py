import sys; input = sys.stdin.readline; INF = float('inf')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

result = INF

for i in range(3):
    dp = [[INF] * 3 for _ in range(n)]

    # 첫 번째 거리 집을 R, G, B 중 하나로 정의
    dp[0][i] = arr[0][i]

    for j in range(1, n):
        dp[j][0] = arr[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = arr[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = arr[j][2] + min(dp[j-1][0], dp[j-1][1])

    for j in range(3):
        if j != i:
            # 첫 번째 집과 다른 색의 집 중 최소 비용
            result = min(result, dp[n-1][j])

print(result)