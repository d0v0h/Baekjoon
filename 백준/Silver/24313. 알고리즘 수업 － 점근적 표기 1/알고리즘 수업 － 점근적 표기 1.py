import sys; input = sys.stdin.readline

a1, a0 = map(int, input().split())
c = int(input())
n_0 = int(input())

if (a1 * n_0 + a0) <= (c * n_0) and a1 <= c:
    print(1)
else:
    print(0)