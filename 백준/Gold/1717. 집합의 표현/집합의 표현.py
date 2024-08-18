import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n+1)]

# 부모 노드를 찾는 함수
def find(node):
    if node == parent[node]:
        return node
    parent[node] = find(parent[node])   # 경로 압축
    return parent[node]

# 노드 연결 함수
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드 연결 확인 함수
def is_connected(a, b):
    if find(a) == find(b):
        return 'YES'
    else:
        return 'NO'

for _ in range(m):
    func, a, b = map(int, input().split())

    if func == 0:
        union(a, b)

    else:
        print(is_connected(a, b))