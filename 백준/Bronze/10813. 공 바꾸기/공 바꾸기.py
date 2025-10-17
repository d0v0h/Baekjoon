n,m=map(int,input().split());b=[i+1 for i in range(n)]
for _ in range(m):
    i,j=map(int,input().split())
    i-=1;j-=1
    b[i],b[j]=b[j],b[i]
print(*b)