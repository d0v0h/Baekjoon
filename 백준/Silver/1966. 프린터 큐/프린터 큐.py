from collections import deque
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    queue = deque([(priority[i], i) for i in range(n)])
    priority.sort(reverse=True)
    cnt = 0
    while queue:
        cur = queue.popleft()
        if cur[0] < priority[cnt]:
            queue.append(cur)
        else:
            cnt += 1
            if cur[1] == m:
                print(cnt)
                break