import sys; input = sys.stdin.readline

arr = [0 for _ in range(4)]

for idx in range(4):
    o, i = map(int, input().split())
    
    if idx == 0:
        arr[idx] += i
    
    elif idx == 3:
        arr[idx] += o
    
    else:
        arr[idx] = arr[idx-1] + (i - o)

print(max(arr))