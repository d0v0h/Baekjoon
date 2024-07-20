import sys
input = sys.stdin.readline

t = int(input())

dp = [0, 1, 1, 1, 2, 2] + [0 for _ in range(96)]
for _ in range(t):
    num = int(input())
    for i in range(6, num+1):
        dp[i] = dp[i-1] + dp[i-5]   # i번째 삼각형은 i-1과 i-5의 삼각형의 빗변을 맞대고 있으므로 더한다.
    print(dp[num])