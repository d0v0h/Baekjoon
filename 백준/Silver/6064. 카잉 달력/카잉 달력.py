import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    M, N, x, y = map(int, input().split())

    k = x
    while k <= M * N:
        if abs(k-y) % N == 0:
            print(k)
            break
        k += M
        y += N
    else:
        print(-1)