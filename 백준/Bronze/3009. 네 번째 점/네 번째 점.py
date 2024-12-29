X=[];Y=[];result=[]
for _ in range(3):
    x,y=map(int,input().split())
    X.append(x);Y.append(y)
for x, y in list(zip(X,Y)):
    if X.count(x)==1:
        result.insert(0,x)
    if Y.count(y)==1:
        result.insert(1,y)
print(*result, sep=' ')