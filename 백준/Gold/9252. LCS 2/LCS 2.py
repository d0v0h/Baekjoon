import sys; input = sys.stdin.readline

a = input().strip()
b = input().strip()

n = len(a)
m = len(b)

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n][m])

if dp[n][m] != 0:
    x, y = n, m
    result = []
    while x > 0 and y > 0:
        if a[x-1] == b[y-1]:
            result.append(a[x-1])
            x -= 1
            y -= 1
        elif dp[x-1][y] > dp[x][y-1]:
            x -= 1
        else:
            y -= 1

    result.reverse()
    print(*result, sep='')