n, m = map(int, input().split())

checker = []
result = []
temp = []

def sol(start):
    if len(temp) == m:
        result.append(temp[:])
        return
    
    for i in range(start, n+1):
        temp.append(i)
        sol(i)
        temp.pop()

sol(1)

for r in result:
    print(*r)