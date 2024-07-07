import sys, heapq
input = sys.stdin.readline

t = int(input())

queue = []
for _ in range(t):
    n = int(input())
    if n != 0:
        heapq.heappush(queue, -1 * n)
    else:
        if len(queue) == 0:
            print(0)
        else:
            print(-1 * heapq.heappop(queue))