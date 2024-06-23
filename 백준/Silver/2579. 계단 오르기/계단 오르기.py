import sys
input = sys.stdin.readline

t = int(input().strip())
arr = [int(input().strip()) for _ in range(t)]
dp = [0] * (t + 1)

dp[0] = arr[0]
if len(arr) >= 2:
    dp[1] = arr[0] + arr[1]

for i in range(2, t):
    dp[i] = max(arr[i] + dp[i-2], arr[i] + arr[i-1] + dp[i-3])

print(dp[t-1])