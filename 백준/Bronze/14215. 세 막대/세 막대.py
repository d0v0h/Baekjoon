a=list(map(int,input().split()))
if max(a) >= sum(a) - max(a):
    a.remove(max(a))
    print(sum(a)*2-1)
else:
    print(sum(a))