import sys
input = sys.stdin.readline

t = int(input())

dp = [0] * 12
for _ in range(t):
    dp[1] = 1   # 1
    dp[2] = 2   # 1+1, 2
    dp[3] = 4   # 1+1+1, 1+2, 2+1, 3
    num = int(input())
    if num < 4:
        print(dp[num])
        continue
    else:
        for i in range(4, num+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    print(dp[num])