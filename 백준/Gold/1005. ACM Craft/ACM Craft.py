from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    build = [0] + list(map(int, input().split()))

    in_degree = [0] * (n+1)
    time = [0] * (n+1)
    graph = [[] for _ in range(n+1)]

    # 노드 연결 지점 입력 및 진입차수 저장
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_degree[b] += 1
    
    obj = int(input())

    # 진입차수 0인 지점 저장
    queue = deque()
    for i in range(1, n+1):
        if in_degree[i] == 0:
            queue.append(i)
            time[i] = build[i]
    
    # 위상 정렬
    while queue:
        node = queue.popleft()

        for next_node in graph[node]:
            in_degree[next_node] -= 1
            time[next_node] = max(time[next_node], time[node] + build[next_node])

            # 진입차수가 0이면 위상정렬에 의해 next_node를 queue에 추가
            if in_degree[next_node] == 0:
                queue.append(next_node)
    
    print(time[obj])