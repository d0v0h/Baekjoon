import sys
input = sys.stdin.readline

t = int(input())
rgb = [list(map(int, input().split())) for _ in range(t)]

dp = [[0] * 3 for _ in range(t)]
dp[0] = rgb[0]

for i in range(1, t):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb[i][2]

print(min(dp[t-1]))