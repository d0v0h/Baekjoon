n=int(input())
a=list(map(int,input().split()))
for i in a:
    if i == 1:
        n-=1
    for j in range(2,i):
        if i % j == 0:
            n-=1
            break
print(n)