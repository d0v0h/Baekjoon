n = int(input())

pp = 1
p = 2
for i in range(3, n+1):
    p, pp = (p + pp) % 15746, p  % 15746

if n != 1:
    print(p % 15746)
else:
    print(1)