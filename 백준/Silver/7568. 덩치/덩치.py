import sys
input = sys.stdin.readline

n = int(input())

result = []
for _ in range(n):
    x, y = map(int, input().split())
    result.append((x, y))

for val in result:
    order = 1
    for comp in result:
        if val[0] < comp[0] and val[1] < comp[1]:
            order += 1
    print(order, end=' ')