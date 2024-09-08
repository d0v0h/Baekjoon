n, a, b = map(int, input().split())

x1 = list(map(int, input().split()))
x2 = list(map(int, input().split()))

x1.sort(reverse=True)
x2.sort(reverse=True)
check = result = 0

if n % 2 == 1:
    result += x1[0]
    x1 = x1[1:]
    check += 1

for i in range(1, n, 2):
    x1_max = x2_max = 0
    if len(x1) >= 2:
        x1_max = x1[0] + x1[1]
    if len(x2) >= 1:
        x2_max = x2[0]
    
    if x1_max > x2_max:
        result += x1_max
        x1 = x1[2:]
    else:
        result += x2_max
        x2 = x2[1:]
    
print(result)