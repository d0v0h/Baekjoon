a = ['a', 'e', 'i', 'o', 'u']

cmd = input()

res = 0
while cmd != '#':
    for c in cmd:
        if c.lower() in a:
            res += 1
    print(res)
    res = 0
    cmd = input()