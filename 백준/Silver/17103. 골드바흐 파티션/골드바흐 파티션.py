import math

prime = [True] * 1000001
prime[0] = prime[1] = False
for i in range(2, 1000001):
    if prime[i] == True:
        for j in range(i * i, 1000001, i):
            prime[j] = False
    

t = int(input())

for _ in range(t):
    n = int(input())
    partition = 0
    for i in range(2, n // 2 + 1):
        if prime[i] and prime[n-i]:
            partition += 1
    print(partition)