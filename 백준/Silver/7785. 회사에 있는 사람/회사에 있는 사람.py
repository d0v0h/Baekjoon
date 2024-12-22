import sys; input = sys.stdin.readline
n = int(input())

dic = {}
for _ in range(n):
    name, cag = input().split()

    if cag == 'enter':
        dic[name] = cag
    else:
        del dic[name]

result = sorted(dic, reverse=True)

print(*result, sep='\n')