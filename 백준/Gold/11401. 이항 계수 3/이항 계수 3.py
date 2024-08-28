def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
        result %= mod
    return result

def dnc(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    temp = dnc(n, k // 2)

    if k % 2 == 0:
        return temp * temp % mod
    else:
        return temp * temp * n % mod
    

n, k = map(int, input().split())
mod = 1000000007

N = factorial(n)
K = factorial(k)
N_K = factorial(n-k)

# a^p = a (mod p)
# a^(p-1) = 1
# a^(p-2) = 1/a => (1/a)를 조합 식의 분모에 적용
# ((N! % mod) * (K!(N-k!)^(mod-2) % mod)) % mod
print(((N * dnc(K * N_K % mod, mod-2)) % mod))