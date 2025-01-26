import sys; input = sys.stdin.readline

n = int(input())
weight = list(map(int, input().split()))

dp = {0}

# 조합 가능한 경우의 수
for w in weight:
    temp = set()
    for item in dp:
        temp.add(item + w); temp.add(abs(item - w))
    dp.update(temp)

m = int(input())
marble = list(map(int, input().split()))

for i in range(m):
    print('Y', end=' ') if marble[i] in dp else print('N', end=' ')