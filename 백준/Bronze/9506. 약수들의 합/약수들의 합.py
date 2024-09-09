n = int(input())

while n != -1:
    temp = []
    for i in range(1, n+1):
        if n % i == 0:
            temp.append(i)
    
    if sum(temp[:-1]) == n:
        print(n, '= ', end='')
        print(*temp[:-1], sep=' + ')
    else:
        print(n, 'is NOT perfect.')
    
    n = int(input())