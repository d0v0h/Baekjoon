# 블로그 참조 코드
from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    num, target = map(int, input().split())

    visited = [False for _ in range(10000)]
    queue = deque()
    queue.append((num, ''))     # num과 해당 num에 도달하게된 cmd를 append
    visited[num] = True

    while queue:
        n, cmd = queue.popleft()

        # target에 도달한 cmd를 출력 (해당 target에 대응되는 최소 cmd를 가지고 있음)
        if n == target:
            print(cmd)
            break

        D = n*2 if n*2 <= 9999 else n*2 % 10000
        if not visited[D]:              # 이미 존재한다면 더 빠른 cmd로 하는 방법이 존재
            visited[D] = True           # 방문 표시
            queue.append((D, cmd+'D'))  # 해당 값에 방문하게 된 cmd를 입력
        
        S = n-1 if n-1 >= 0 else 9999
        if not visited[S]:
            visited[S] = True
            queue.append((S, cmd+'S'))
        
        L = (n  * 10 % 10000) + (n // 1000) 
        if not visited[L]:
            visited[L] = True
            queue.append((L, cmd+'L'))

        R = (n // 10) + (n % 10 * 1000)
        if not visited[R]:
            visited[R] = True
            queue.append((R, cmd+'R'))