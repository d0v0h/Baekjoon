import sys
n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

# 뒤에서부터 누적 합 계산
for i in range(n - 2, -1, -1):
    a[i] += a[i + 1]

# 목표 M을 달성하는 최소 일수 찾기
for i in range(n - 1, -1, -1):
    if a[i] >= m:
        print(i + 1)
        exit()

print(-1)