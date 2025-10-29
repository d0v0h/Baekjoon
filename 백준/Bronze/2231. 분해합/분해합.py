n=int(input())
for i in range(n):
    temp = i + sum([int(j) for j in str(i)])
    if temp == n:
        print(i)
        break
else:
    print(0)