h,m=map(int,input().split())
early=m-45
if early < 0:
    if h == 0:
        print(23, 60 + early)
    else:
        print(h-1, 60 + early)
else:
    print(h, early)