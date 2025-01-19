import sys; input = sys.stdin.readline

n = int(input())
result = 0

x1, y1 = map(int, input().split())
first_x, first_y = x1, y1
for _ in range(1, n):
    x2, y2 = map(int, input().split())
    result += x1*y2 - x2*y1
    x1, y1 = x2, y2
result += x2 * first_y - y2 * first_x

print(abs(result) / 2)