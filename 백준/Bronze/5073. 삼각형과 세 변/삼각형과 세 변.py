a, b, c = map(int, input().split())

while a and b and c:
    d = [a, b, c]; max_d = max(d); d.remove(max_d)

    if a == b and b == c:  print('Equilateral')
    elif max_d >= sum(d):    print('Invalid')
    elif a != b and b != c and a != c:  print('Scalene')
    else: print('Isosceles')

    a, b, c = map(int, input().split())