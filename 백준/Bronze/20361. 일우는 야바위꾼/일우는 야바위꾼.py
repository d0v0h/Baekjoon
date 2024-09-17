import sys; input = sys.stdin.readline

n, x, k = map(int, input().split())

arr = [0 for _ in range(n+1)]
arr[x] = 1
for _ in range(k):
    a, b = map(int, input().split())
    
    arr[a], arr[b] = arr[b], arr[a]

print(arr.index(1))