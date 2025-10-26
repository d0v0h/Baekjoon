m=int(input())
n=int(input())
r=[]
for i in range(m,n+1):
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            r.append(i)
print(sum(r), min(r), sep='\n') if len(r) != 0 else print(-1)