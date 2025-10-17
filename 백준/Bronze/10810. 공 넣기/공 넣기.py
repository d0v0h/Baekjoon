n,m=map(int,input().split());b=[0 for _ in range(n)]
for i in range(m):
    i,j,k=map(int,input().split())
    b[i-1:j]=[k]*(j-i+1)
print(*b)