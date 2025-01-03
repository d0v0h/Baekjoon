n = int(input())

check = {'ChongChong'}
for _ in range(n):
    a, b = input().split()

    if b in check:
        check.add(a)
    elif a in check:
        check.add(b)

print(len(check))