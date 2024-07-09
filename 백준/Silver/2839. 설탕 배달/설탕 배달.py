n = int(input())

if n % 5 == 0:
    print(int(n/5))
else:
    res = 0
    while n >= 0:
        n -= 3
        res += 1
        if n % 5 == 0:
            res += int(n/5)
            print(res)
            break
    else:
        print(-1)