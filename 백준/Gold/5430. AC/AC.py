from collections import deque
import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    cmd = input().strip()
    arr_length = int(input().strip())
    arr = input().strip()[1:-1].split(',')

    arr = deque(arr) if arr_length > 0 else []

    R_count = 0
    Flag = False

    for word in cmd:
        if word == 'R':
            R_count += 1
        else:
            if len(arr) == 0:
                print('error')
                Flag = True
                break
            elif R_count % 2 == 0:
                arr.popleft()
            else:
                arr.pop()

    if not Flag:
        if R_count % 2 == 1:
            arr.reverse()
        print('[' + ','.join(arr) + ']')