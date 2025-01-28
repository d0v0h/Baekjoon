import sys; input = sys.stdin.readline
from collections import deque

def sol():
    if m == 0:
        print(*rank)
        return
    
    # 위상 정렬 진입 차수 설정
    queue = deque()
    for i in range(1, n+1):
        if in_degree[i] == 0:
            queue.append(i)
    if len(queue) == 0:
        # 사이클 존재
        print('IMPOSSIBLE')
        return
    
    result = []
    while queue:
        cur = queue.popleft()
        result.append(cur)
        for neighbor in graph[cur]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    print(*result) if sum(in_degree) == 0 else print("IMPOSSIBLE")
    return

t = int(input())
for _ in range(t):
    n = int(input())
    rank = list(map(int, input().split()))
    in_degree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for i in range(n):
        # 진입 차수 및 그래프 간선 설정
        graph[rank[i]] = rank[i+1:]
        in_degree[rank[i]] = i
    
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if a in graph[b]:
            graph[a].append(b)
            in_degree[a] -= 1

            graph[b].remove(a)
            in_degree[b] += 1
        else:
            graph[a].remove(b)
            in_degree[a] += 1

            graph[b].append(a)
            in_degree[b] -= 1

    sol()
