from collections import deque
import sys; input = sys.stdin.readline

n = int(input())

queue = deque()
for _ in range(n):
    inputs = input().split()

    cmd = int(inputs[0])
    num = int(inputs[1]) if len(inputs) > 1 else None

    if cmd == 1:
        queue.appendleft(num)
    
    elif cmd == 2:
        queue.append(num)
    
    elif cmd == 3:
        print(queue.popleft()) if queue else print(-1)
    
    elif cmd == 4:
        print(queue.pop()) if queue else print(-1)

    elif cmd == 5:
        print(len(queue))
    
    elif cmd == 6:
        print(1) if len(queue) == 0 else print(0)
    
    elif cmd == 7:
        print(queue[0]) if queue else print(-1)
    
    else:
        print(queue[-1]) if queue else print(-1)