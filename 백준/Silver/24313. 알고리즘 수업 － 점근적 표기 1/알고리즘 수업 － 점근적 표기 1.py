a1,a0,c,n0=map(int,open(0).read().split())
if c >= a1 and a1*n0+a0 <= c*n0:
    print(1)
else:
    print(0)