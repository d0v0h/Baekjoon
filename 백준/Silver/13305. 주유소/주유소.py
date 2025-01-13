import sys; input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
oil = list(map(int, input().split()))[:-1]

min_oil = 1_000_000_001
result = 0
for i in range(n-1):
    if oil[i] < min_oil:
        min_oil = oil[i]
    result += min_oil * dist[i]
print(result)