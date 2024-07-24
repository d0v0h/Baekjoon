# 블로그 참조 공부
import sys
input = sys.stdin.readline
n = int(input())

dp = [1e9] * (n+1)
dp[0] = 0   # 0을 참조하게 되는 경우 i는 j*j가 되는 경우이다.

for i in range(1, n+1):
    j = 1
    while j*j <= i:
        dp[i] = min(dp[i], dp[i-j*j]+1)     # 표현 가능한 수에서 하나 추가
        j += 1

print(dp[n])