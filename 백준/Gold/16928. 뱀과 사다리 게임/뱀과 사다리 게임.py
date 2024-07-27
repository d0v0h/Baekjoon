from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ladder = {}
for _ in range(n):
    a, b = map(int, input().split())
    ladder[a] = b

snake = {}
for _ in range(m):
    a, b = map(int, input().split())
    snake[a] = b

queue = deque()
visited = [False] * 101
cnt = [0] * 101
def BFS():
    queue.append(1)
    visited[1] = True

    while queue:
        node = queue.popleft()

        if node == 100:
            print(cnt[100])
            break

        for i in range(1, 6+1):
            next_node = node + i

            if next_node <= 100 and not visited[next_node]:

                # 사다리로 이동할 경우
                if next_node in ladder.keys():
                    next_node = ladder[next_node]

                # 뱀으로 이동할 경우
                elif next_node in snake.keys():
                    next_node = snake[next_node]

                # 사다리, 뱀으로 이동하고도 한번도 방문하지 않은 경우
                if not visited[next_node]:
                    queue.append(next_node)
                    visited[next_node] = True
                    cnt[next_node] = cnt[node] + 1

BFS()