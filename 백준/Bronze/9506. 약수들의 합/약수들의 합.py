n=int(input())
while n != -1:
    r=[]
    for i in range(1,n):
        if n % i == 0:
            r.append(i)
    print(f"{n} =", ' + '.join(map(str,r))) if sum(r) == n else print(f"{n} is NOT perfect.")
    n=int(input())