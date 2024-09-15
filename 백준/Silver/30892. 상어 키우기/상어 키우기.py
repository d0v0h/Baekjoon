n, k, t = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

cnt = 0
i = 0
stack = []

while cnt < k:
    if i < len(arr) and arr[i] < t:
        stack.append(arr[i])
        i += 1
    elif stack:
        t += stack.pop()
        cnt += 1
    else:
        break

print(t)