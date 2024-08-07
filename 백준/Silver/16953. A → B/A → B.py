from collections import deque

a, b = map(int, input().split())

queue = deque()
def BFS(n):
    queue.append((n, 1))

    while queue:
        num, cnt = queue.popleft()
        if num == b:
            print(cnt)
            break
        elif num < b:
            queue.append((num*2, cnt+1))
            queue.append((num*10+1, cnt+1))
    else:
        print(-1)
BFS(a)