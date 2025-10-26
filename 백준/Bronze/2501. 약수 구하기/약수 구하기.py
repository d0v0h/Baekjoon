a,b=map(int,input().split());r=[]
for i in range(1,a+1):
    if a % i == 0:
        r.append(i)
try:
    print(r[b-1])
except:
    print(0)