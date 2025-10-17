n,x=map(int,input().split())
a=list(map(int,input().split()))
print(*[i for i in a if i < x])