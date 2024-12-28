import sys; input = sys.stdin.readline

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

t = int(input())

interval = []

temp = int(input())
for i in range(1, t):
    tree = int(input())
    interval.append(tree - temp)
    temp = tree

fit_inter = interval[0]
for i in range(1, len(interval)):
    fit_inter = gcd(fit_inter, interval[i])

result = 0
for item in interval:
    item -= fit_inter
    item //= fit_inter
    result += item
print(result)