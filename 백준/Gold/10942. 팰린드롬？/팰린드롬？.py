import sys; input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

dp = [[0] * n for _ in range(n)]

# 자기 자신은 팰린드롬
for i in range(n):
    dp[i][i] = 1

# 길이가 2인 팰린드롬
for i in range(n-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1

# 길이가 3 이상인 팰린드롬
for length in range(3, n + 1):
    for start in range(n - length + 1):
        end = start + length - 1
        if arr[start] == arr[end] and dp[start+1][end-1] == 1:
            dp[start][end] = 1

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])