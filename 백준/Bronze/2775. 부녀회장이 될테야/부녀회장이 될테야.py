import sys
input = sys.stdin.readline

t = int(input())

dp = [[i for i in range(14+1)] for _ in range(14+1)]

for i in range(1, 14+1):
    for j in range(1, 14+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

for _ in range(t):
    k = int(input())
    n = int(input())
    print(dp[k][n])