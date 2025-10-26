n=int(input())
r=[];i=2
while n > 1:
    if n % i == 0:
        n /= i
        r.append(i)
    else:
        i += 1
print(*r, sep='\n')