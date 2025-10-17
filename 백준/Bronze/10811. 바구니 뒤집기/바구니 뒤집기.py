n,m=map(int,input().split());b=[i+1 for i in range(n)]
for i in range(m):
    i,j=map(int,input().split())
    b[i-1:j]=b[i-1:j][::-1]
print(*b)