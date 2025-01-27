from collections import deque
import sys; input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
check = dict()
for item in arr:
    if item in check:
        check[item] += 1
    else:
        check[item] = 1

stack = [arr[-1]]
answer = deque([-1])

for i in range(n - 2, -1, -1):
    while stack and check[arr[i]] >= check[stack[-1]]:
        stack.pop()
    
    if stack:
        answer.appendleft(stack[-1])
    
    else:
        answer.appendleft(-1)

    stack.append(arr[i])

print(*answer)