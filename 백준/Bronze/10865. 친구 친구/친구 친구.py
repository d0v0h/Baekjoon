import sys
input = sys.stdin.readline

n, m = map(int, input().split())

std = {}
for i in range(1, n+1):
    std[i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    std[a] += 1
    std[b] += 1

for value in std.values():
    print(value)