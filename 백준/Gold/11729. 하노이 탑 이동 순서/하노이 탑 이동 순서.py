k = int(input())

result = []
def tower(n, start, temp, end):
    if n == 1:
        result.append((start, end))
        return
    
    tower(n-1, start, end, temp)
    result.append((start, end))
    tower(n-1, temp, start, end)

tower(k, 1, 2, 3)
print(len(result))
for r in result:
    print(*r)