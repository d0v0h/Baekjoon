import math

n, r = map(int, input().split())

x_list = []
y_list = []
for _ in range(n):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

x_min = min(x_list)
x_max = max(x_list)

y_min = min(y_list)
y_max = max(y_list)

max_cnt = -1
result = []
for x in range(x_min, x_max +1):
    for y in range(y_min, y_max+1):
        temp_cnt = 0

        for nx, ny in zip(x_list, y_list):
            if math.sqrt((x - nx) ** 2 + (y - ny) ** 2) <= r:
                temp_cnt += 1
    
        if temp_cnt > max_cnt:
            max_cnt = temp_cnt
            result = [x, y]

print(*result)