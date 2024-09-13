x, y = map(int, input().split())

x_bit = []
for i in range(1, x+1):
    x_bit.append(i/x)

y_bit = []
for i in range(1, y+1):
    y_bit.append(i/y)

result = []
while len(x_bit) or len(y_bit):
    if x_bit[0] < y_bit[0]:
        x_bit = x_bit[1:]
        result.append(1)
    elif y_bit[0] < x_bit[0]:
        y_bit = y_bit[1:]
        result.append(2)
    else:
        x_bit = x_bit[1:]
        y_bit = y_bit[1:]
        result.append(3)

print(*result, sep='')