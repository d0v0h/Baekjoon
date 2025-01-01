from collections import deque
import sys; input = sys.stdin.readline

n = int(input())

queue = deque()
for _ in range(n):
    inputs = input().split()

    cmd = inputs[0]
    num = int(inputs[1]) if len(inputs) > 1 else None

    if cmd == 'push':
        queue.append(num)
    
    elif cmd == 'pop':
        print(queue.popleft()) if queue else print(-1)

    elif cmd == 'size':
        print(len(queue))
    
    elif cmd == 'empty':
        print(1) if len(queue) == 0 else print(0)
    
    elif cmd == 'front':
        print(queue[0]) if queue else print(-1)
    
    else:
        print(queue[-1]) if queue else print(-1)