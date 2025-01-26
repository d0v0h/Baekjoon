from collections import deque
import sys; input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

answer = deque()
stack = []

for i in range(n - 1, -1, -1):
    while stack and stack[-1] <= arr[i]:
        stack.pop()
    
    if stack:
        answer.appendleft(stack[-1])

    else:
        answer.appendleft(-1)
    stack.append(arr[i])

print(*answer)