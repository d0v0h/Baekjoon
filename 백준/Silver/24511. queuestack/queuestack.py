from collections import deque
import sys; input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

queue = deque()
for idx, elem in enumerate(A):
    if elem == 0:
        queue.appendleft(B[idx])

for i in range(M):
    queue.append(C[i])
    print(queue.popleft(), end=' ')