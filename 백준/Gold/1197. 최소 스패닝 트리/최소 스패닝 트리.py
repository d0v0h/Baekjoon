import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())

# 부모 노드 명시
parent = [i for i in range(n+1)]

# 간선과 가중치를 추가. (가중치를 오름차순으로 정렬)
queue = []
for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(queue, (c, a, b))

def find(node):
    if node == parent[node]:
        return node
    parent[node] = find(parent[node])   # 경로 압축
    return parent[node]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edge = 0
result = 0

while edge < n-1:
    w, s, e = heapq.heappop(queue)
    # 만약 둘의 부모노드가 다르면 (다른 집합으로 사이클이 아니라면)
    if find(s) != find(e):
        # 연결
        union(s, e)
        result += w
        edge += 1

print(result)