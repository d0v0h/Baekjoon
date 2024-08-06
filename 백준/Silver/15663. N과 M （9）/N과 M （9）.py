import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

temp = []
result = []

def sol():
    if len(temp) == m:
        result.append(temp[:])
        return
    
    prev = -1
    for i in range(n):
        if not visited[i] and arr[i] != prev:
            visited[i] = True
            temp.append(arr[i])
            prev = arr[i]
            sol()
            temp.pop()
            visited[i] = False

visited = [False] * n
sol()

for ans in result:
    print(*ans)