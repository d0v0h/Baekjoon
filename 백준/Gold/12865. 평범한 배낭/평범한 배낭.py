import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = []
for _ in range(n):
    w, v = map(int, input().split())
    arr.append((w, v))

dp = [0 for _ in range(k+1)]
for w, v in arr:
    # 오름차순으로 반복하면 이전 아이템을 사용할 가능성이 있으므로 역순으로 진행
    for i in range(k, w-1, -1):
        if dp[i] < dp[i-w] + v:
            dp[i] = dp[i-w] + v

print(max(dp))