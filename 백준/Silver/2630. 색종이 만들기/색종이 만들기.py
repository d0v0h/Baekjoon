import sys
input = sys.stdin.readline

t = int(input().strip())

graph = []
for _ in range(t):
    arr = list(map(int, input().split()))
    graph.append(arr)

blue = 0
white = 0

def cut(x, y, N):
    global blue, white
    color = graph[x][y]
    for nx in range(x, x + N):
        for ny in range(y, y + N):
            if color != graph[nx][ny]:
                cut(x, y, N // 2)
                cut(x + (N // 2), y, N // 2)
                cut(x, y + (N // 2), N // 2)
                cut(x + (N // 2), y + (N // 2), N // 2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

cut(0, 0, t)
print(white)
print(blue)