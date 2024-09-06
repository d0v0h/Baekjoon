import sys; input = sys.stdin.readline

n, m, k = map(int, input().split())
dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))

hands = [0 for _ in range(n)]

check = 0
for j in range(m):
    for i in range(n):
        hands[i] += dp[i][j]

        if hands[i] >= k:
            print(i+1, j+1)
            exit()