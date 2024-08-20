import sys, heapq
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


n, m = map(int, input().split())

parent = [i for i in range(n+1)]

queue = []
for _ in range(m):
    a, b, w = map(int, input().split())
    heapq.heappush(queue, (w, a, b))

edge = 0
result = 0

while edge < n-2:
    w, a, b = heapq.heappop(queue)
    if find(a) != find(b):
        union(a, b)
        result += w
        edge += 1
    
print(result)
