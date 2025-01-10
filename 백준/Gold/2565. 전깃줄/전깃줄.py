t = int(input())

arr = [list(map(int, input().split())) for _ in range(t)]
arr.sort(key = lambda x: x[0])

dp = [1] * t
for i in range(1, t):
    for j in range(i):
        if arr[j][1] < arr[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(t - max(dp))