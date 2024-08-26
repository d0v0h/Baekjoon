def recursion(n):
    if n == 3:
        return ['***', '* *', '***']
    temp = recursion(n // 3)

    result = []
    for t in temp:
        result.append(t * 3)
    for t in temp:
        result.append(t + ' ' * (n // 3) + t)
    for t in temp:
        result.append(t * 3)
    
    return result

n = int(input())

result = recursion(n)

for r in result:
    print(*r, sep='')