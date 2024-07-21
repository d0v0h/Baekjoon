import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coin = []
for _ in range(n):
    num = int(input())
    if num <= k:
        coin.append(num)

remain = 0
while k:
    i = coin[-1]
    remain += k // i
    k %= i
    coin.pop()

print(remain)