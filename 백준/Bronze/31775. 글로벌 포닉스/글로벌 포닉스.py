check = set()
for _ in range(3):
    a = input()
    check.add(a[0])

answer = ['l', 'p', 'k']
if len(check) == 3:
    for c in check:
        if c not in answer:
            print('PONIX')
            break
    else:
        print('GLOBAL')
else:
    print('PONIX')