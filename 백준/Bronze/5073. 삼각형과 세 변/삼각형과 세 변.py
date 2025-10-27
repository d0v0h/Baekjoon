a=list(map(int,input().split()))
while sum(a) != 0:
    m=max(a)
    r=sum(a)-m
    if m >= r:
        print("Invalid")
    else:
        if a[0] == a[1] == a[2]:
            print("Equilateral")
        elif a[0] != a[1] and a[1] != a[2] and a[0] != a[2]:
            print("Scalene")
        else:
            print("Isosceles")
    a=list(map(int,input().split()))