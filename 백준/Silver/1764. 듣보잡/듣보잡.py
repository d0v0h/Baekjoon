import sys
input = sys.stdin.readline
n, m = map(int, input().split())

dict = {}
for i in range(n):
    not_listen = input().strip()
    if not_listen not in dict:
        dict[not_listen] = 1

result = []
for i in range(m):
    not_see = input().strip()
    if not_see in dict:
        result.append(not_see)

result.sort()
print(len(result))
for i in result:
    print(i)