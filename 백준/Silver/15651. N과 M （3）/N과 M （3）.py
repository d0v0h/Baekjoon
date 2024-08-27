n, m = map(int, input().split())

result = []

def sol():
    if len(result) == m:
        print(*result)
        return
    
    for i in range(1, n+1):
        result.append(i)
        sol()
        result.pop()
    
sol()