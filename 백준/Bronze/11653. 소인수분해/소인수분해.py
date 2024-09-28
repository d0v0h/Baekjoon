n = int(input())
m = 2

result = []
while n != 1:
    if n % m == 0:
        n //= m
        result.append(m)
        m = 2
    else:
        m += 1

print(*result, sep='\n')