import sys; input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

stack = []; result = 0
for i in range(n):
    count = 1
    while stack and arr[i] >= stack[-1][0]:
        h, c = stack.pop()
        result += c

        if arr[i] == h:
            count += c
    
    if stack: result += 1

    stack.append((arr[i], count))

print(result)