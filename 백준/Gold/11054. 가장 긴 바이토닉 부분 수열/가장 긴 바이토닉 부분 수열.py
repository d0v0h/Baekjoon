import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

ascen_dp = [1] * n
dscen_dp = [1] * n

# 앞에서 증가하는 부분 체크 (i는 현재 바라보는 문자, j는 앞의 문자를 확인)
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            ascen_dp[i] = max(ascen_dp[j]+1, ascen_dp[i])

# 뒤에서 증가하는 부분 체크
for i in range(n-2, -1, -1):
    for j in range(n-1, i, -1):
        if arr[i] > arr[j]:
            dscen_dp[i] = max(dscen_dp[j]+1, dscen_dp[i])

# 증가, 감소 dp에 대해 인덱스를 참조가 긴 바이토닉을 찾음
ans = 0
for i in range(n):
    ans = max(ans, ascen_dp[i] + dscen_dp[i])

# i지점까지 동일한 지점에 2번 계산되므로 1을 뺌
print(ans-1)