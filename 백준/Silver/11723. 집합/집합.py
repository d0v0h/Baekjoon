import sys
input = sys.stdin.readline

s = []

n = int(input())

for _ in range(n):
    cmd_arr = input().split()

    if len(cmd_arr) == 2:
        cmd = cmd_arr[0]
        num = int(cmd_arr[1])
    else:
        cmd = cmd_arr[0]
    if cmd == 'add':
        if num in s:
            pass
        else:
            s.append(num)
    elif cmd == 'remove':
        if num in s:
            s.remove(num)
        else:
            pass
    elif cmd == 'check':
        if num in s:
            print(1)
        else:
            print(0)
    elif cmd == 'toggle':
        if num in s:
            s.remove(num)
        else:
            s.append(num)
    elif cmd == 'all':
        s = [i for i in range(1,20+1)]
    else:
        s = []
