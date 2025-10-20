o=[1,1,2,2,2,8]
n=list(map(int,input().split()))
print(*[i-j for i,j in zip(o,n)])