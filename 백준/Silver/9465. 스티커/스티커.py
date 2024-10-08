from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        print(max(map(max, dp)))
        continue

    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]

    for j in range(2, n):
        for i in range(2):
            if i == 0:
                dp[i][j] += max(dp[i+1][j-1], max(dp[0][j-2], dp[1][j-2]))
            else:
                dp[i][j] += max(dp[i-1][j-1], max(dp[0][j-2], dp[1][j-2]))
            
    print(max(map(max, dp)))