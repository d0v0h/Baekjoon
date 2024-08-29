import sys; input = sys.stdin.readline

code = input().strip()

n = int(input())

result = 0
for _ in range(n):
    re_cor = input().strip()

    if code[:5] == re_cor[:5]:
        result += 1

print(result)