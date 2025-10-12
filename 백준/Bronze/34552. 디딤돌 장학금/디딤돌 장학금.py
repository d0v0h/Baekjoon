import sys; input = sys.stdin.readline

credit = list(map(int, input().split()))
n = int(input())

answer = 0
for i in range(n):
    b, l, s = list(map(float, input().split()))
    if l >= 2.0 and s >= 17:
        answer += credit[int(b)]

print(answer)