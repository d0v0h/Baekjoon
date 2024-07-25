import sys
input = sys.stdin.readline

n, m = map(int, input().split())

memo = {}

for _ in range(n):
    site, pw = input().split()
    memo[site] = pw

result = []
for _ in range(m):
    site = input().strip()
    result.append(memo[site])

print(*result, sep='\n')