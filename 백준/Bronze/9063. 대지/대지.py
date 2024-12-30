t=int(input())
x_max=y_max=-10001; x_min=y_min=10001
for _ in range(t):
    x, y = map(int, input().split())
    x_min = min(x_min, x); y_min = min(y_min, y)
    x_max = max(x_max, x); y_max = max(y_max, y)
print((x_max-x_min)*(y_max-y_min))