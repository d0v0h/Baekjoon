import sys
input = sys.stdin.readline

n = int(input())
max_dp = list(map(int, input().split()))
min_dp = max_dp[:]

for i in range(1, n):
    arr = list(map(int, input().split()))
    temp_max = max_dp[:]
    temp_min = min_dp[:]
    max_dp[0] = arr[0] + max(temp_max[0], temp_max[1])
    max_dp[1] = arr[1] + max(temp_max[0], temp_max[1], temp_max[2])
    max_dp[2] = arr[2] + max(temp_max[1], temp_max[2])

    min_dp[0] = arr[0] + min(temp_min[0], temp_min[1])
    min_dp[1] = arr[1] + min(temp_min[0], temp_min[1], temp_min[2])
    min_dp[2] = arr[2] + min(temp_min[1], temp_min[2])

print(max(max_dp), min(min_dp))