a, b = map(int, input().split())
temp = a*b
while b != 0:
    a, b = b, a % b
print(a, temp//a, sep='\n')