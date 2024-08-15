import sys
sys.setrecursionlimit(10**9)

mod = 1_000_000_007

m = int(input())

def cal_spuare(n, power):
    if power == 0:
        return 1
    
    if power == 1:
        return n
    
    temp = cal_spuare(n, power//2)
    if power % 2 == 0:
        return temp * temp % mod
    else:
        return temp * temp * n % mod

result = 0
for _ in range(m):
    n, s = map(int, input().split())
    # a * b^(-2) % 1_000_000_007
    b = cal_spuare(n, mod-2)
    result += ((s*b)%mod)
    result %= mod

print(result)