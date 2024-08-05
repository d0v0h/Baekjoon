import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
dp = [1] * n

for i in range(1, len(A)):
    max_cnt = 0
    for j in range(i):
        if A[i] > A[j]:
            if dp[j] > max_cnt:
                max_cnt = dp[j]
                dp[i] = dp[j] + 1

print(max(dp))