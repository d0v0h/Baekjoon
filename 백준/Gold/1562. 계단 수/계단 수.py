import sys; input = sys.stdin.readline

n = int(input())

dp = [[[0] * 1024 for _ in range(10)] for _ in range(n+1)]

# n이 1일때의 방문값 초기화
for i in range(10):
    dp[1][i][1 << i] = 1

for i in range(2, n+1):
    for j in range(10):
        for k in range(1024):
            if j == 0:
                # n = 2, j = 0, k = 2를 기준으로 dp[2][0][00_0000_0011] += dp[1][1][00_0000_0010]
                # (1 << j)는 현재 j의 비트를 표현
                dp[i][j][(1 << j) | k] += dp[i-1][j+1][k]
            elif j == 9:
                dp[i][j][(1 << j) | k] += dp[i-1][j-1][k]
            else:
                dp[i][j][(1 << j) | k] += (dp[i-1][j-1][k] + dp[i-1][j+1][k])
            dp[i][j][(1 << j) | k] %= 1000000000

result = 0
for i in range(1, 10):
    result += dp[n][i][1023]

print(result % 1000000000)