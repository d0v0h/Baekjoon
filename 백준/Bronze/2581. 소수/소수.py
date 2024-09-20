m = int(input())
n = int(input())

result = []
for i in range(m, n+1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            result.append(i)

if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)