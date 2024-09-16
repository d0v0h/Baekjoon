n, m = map(int, input().split())

result = []
for i in range(n):
    color = list(input())

    for i in range(m):
        if color[i] != '.':
            color[m-1-i] = color[i]
    
    result.append(color)

for r in result:
    print(*r, sep='')