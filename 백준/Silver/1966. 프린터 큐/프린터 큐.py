from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))

    queue = deque([(priority[i], i) for i in range(n)])
    priority.sort(reverse=True)

    cnt = 0
    while queue:
        cur = queue.popleft()
        # 우선 순위가 낮으면
        if cur[0] < priority[cnt]:
            queue.append(cur)    # 뒤로 보냄
        # 우선 순위에 충족하면
        else:
            cnt += 1    # 다음 우선 순위로 넘어감
            if cur[1] == m:    # 만약 꺼낸 값이 m과 일치하면
                print(cnt)     # 횟수 출력
                break