from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

graph = [0] * (10**5 + 1)
visited = [False] * (10**5 + 1)
queue = deque()

def BFS(start, end):
    queue.append(start)
    global min_cnt, total_cnt

    if start == end:
        min_cnt = 0
        total_cnt = 1
        return
    
    while queue:
        node = queue.popleft()
        visited[node] = True

        if node == end:
            if graph[node] < min_cnt:
                min_cnt = graph[node]
                total_cnt = 1
            elif graph[node] == min_cnt:
                total_cnt += 1

        for x in (node-1, node+1, node*2):
            if 0 <= x <= 10**5:
                # graph[x] >= graph[node] + 1 조건을 추가하여 더 적은 방문횟수의 x를 queue에 추가
                if not visited[x] or graph[x] >= graph[node] + 1:
                    visited[x] = True
                    graph[x] = graph[node] + 1
                    queue.append(x)

min_cnt = 1e9
total_cnt = 0
BFS(n, k)
print(min_cnt, total_cnt, sep='\n')