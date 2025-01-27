import sys; input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)] + [0]

stack = [(0, arr[0])]   # idx와 height 저장
result = 0

for i in range(1, len(arr)):
    start = i
    while stack and stack[-1][1] > arr[i]:
        idx, height = stack.pop()
        result = max(result, (i - idx) * height)
        start = idx
    stack.append((start, arr[i]))

print(result)