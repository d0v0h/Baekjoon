import sys; input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    files = list(map(int, input().split()))

    # 한 칸씩 누적합
    prefix_sum = [0] * (k+1)
    for i in range(1, k + 1):
        prefix_sum[i] = prefix_sum[i-1] + files[i-1]
    
    dp = [[0 for _ in range(k+1)] for _ in range(k+1)]

    # dp[i][j] => i번 file에서 j번 file의 합
    for count in range(2, k+1):
        for i in range(1, k - count + 2):
            j = i + count - 1
            dp[i][j] = float('inf')
            for m in range(i, j):
                # 점화식: dp[i][j] => dp[i][m] + dp[m+1][j] 중 최소 값
                dp[i][j] = min(dp[i][j], dp[i][m] + dp[m+1][j] + prefix_sum[j] - prefix_sum[i-1])
    
    print(dp[1][k])
