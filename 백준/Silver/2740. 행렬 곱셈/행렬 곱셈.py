import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

m, k = map(int, input().split())
B = []
for _ in range(m):
    B.append(list(map(int, input().split())))

result = [[0]*k for _ in range(n)]
for i in range(n):
    for j in range(k):
        for t in range(m):
            result[i][j] += A[i][t] * B[t][j]

for r in result:
    print(*r)