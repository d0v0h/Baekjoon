from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
in_degree = [0 for _ in range(n+1)]

for _ in range(m):
    A, B = map(int, input().split())
    graph[A].append(B)    # A -> B 명시
    in_degree[B] += 1     # 진입차수 증가

queue = deque()
for i in range(1, n+1):
    # 진입차수가 없는 노드를 queue에 추가
    if in_degree[i] == 0:
        queue.append(i)

for _ in range(n):
    # 처음 순서의 노드를 queue에서 꺼냄
    node = queue.popleft()
    print(node, end=' ')
    # 연결된 노드를 호출
    for next_node in graph[node]:
        in_degree[next_node] -= 1     # 처음 노드를 진입차수에서 제외하므로 1 감소
        # 만약 진입차수가 없다면
        if in_degree[next_node] == 0:
            queue.append(next_node)    # queue에 추가
            