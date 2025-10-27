a=list(map(int,open(0).read().split()))
if sum(a) != 180:
    print("Error")
else:
    if a[0] == a[1] and a[1] == a[2]:
        print("Equilateral")
    elif a[0] != a[1] and a[1] != a[2] and a[0] != a[2]:
        print("Scalene")
    else:
        print("Isosceles")