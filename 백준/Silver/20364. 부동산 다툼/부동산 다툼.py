import sys; input = sys.stdin.readline

n, q = map(int, input().split())
visitied = [False for _ in range(n+1)]

for _ in range(q):
    v = int(input())
    temp = v
    blocked = 0
    
    while temp > 1:
        if visitied[temp]:
            blocked = temp
        temp //= 2
        
    if blocked == 0:
        print(0)
        visitied[v] = True
    else:
        print(blocked)