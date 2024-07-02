import sys
input = sys.stdin.readline

t = int(input())
dp = []

for i in range(t):
    num = list(map(int, input().split()))
    dp.append(num)

for i in range(1, t):
    for j in range(i+1):
        if j == 0:
            dp[i][j] += dp[i-1][j]
        elif j == i:
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[-1]))