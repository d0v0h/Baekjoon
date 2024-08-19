import sys
input = sys.stdin.readline

def find(node):
    if node == parent[node]:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())

parent = [i for i in range(n+1)]

for i in range(1, n+1):
    town = list(map(int, input().split()))
    for j in range(len(town)):
        if town[j] == 1:
            union(i, j+1)

dest = list(map(int, input().split()))
check = find(dest[0])

for path in dest[1:]:
    if check != find(path):
        print('NO')
        break
else:
    print('YES')