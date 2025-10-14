a = int(input())
b = input().strip()

for i in b[::-1]:
    print(a * int(i))
print(a*int(b))