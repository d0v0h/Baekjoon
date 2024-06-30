def modulo(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (modulo(a, b//2, c) ** 2) % c
    else:
        return ((modulo(a, b//2, c) ** 2) * a) % c

a, b, c = map(int, input().split())
print(modulo(a, b, c))