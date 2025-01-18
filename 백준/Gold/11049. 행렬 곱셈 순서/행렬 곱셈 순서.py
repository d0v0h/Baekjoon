import sys; input = sys.stdin.readline

n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]

for l in range(1, n):
    for i in range(n - l):
        j = i + l
        dp[i][j] = float('inf')

        for m in range(i, j):
            dp[i][j] = min(dp[i][m] + dp[m+1][j] + matrix[i][0] * matrix[m][1] * matrix[j][1], dp[i][j])
    
print(dp[0][-1])