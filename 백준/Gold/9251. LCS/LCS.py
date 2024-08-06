import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()

dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]

for i, c1 in enumerate(s1, start=1):
    for j, c2 in enumerate(s2, start=1):
        if c1 == c2:
            # 두 문자가 같은 경우 대각선에 위치한 수열 정보에 1을 더함
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            # 두 문자가 같지 않은 경우 이전까지 가장 긴 수열 정보를 가져옴
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(max(map(max, dp)))