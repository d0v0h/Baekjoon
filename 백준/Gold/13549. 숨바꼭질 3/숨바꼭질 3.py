from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

graph = [0] * (10**5 + 1)
visited = [0] * (10**5 + 1)

queue = deque()
def BFS(start, end):
    queue.append(start)

    if start == end:
        print(0)
        return
    
    while queue:
        node = queue.popleft()
        visited[node] = True

        if node == end:
            print(graph[node])
            return

        for x in (node*2, node-1, node+1):
            if 0 <= x <= 10**5:
                if not visited[x]:
                    queue.append(x)
                    visited[x] = True
                    if x == node*2:
                        graph[x] = graph[node]
                    else:
                        graph[x] = graph[node] + 1

BFS(n, k)