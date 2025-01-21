n = int(input())

if n == 1:
    print('0')
    exit(0)

prime = [True] * (n+1)
prime[0] = prime[1] = False

# 소수 계산
for i in range(2, int(n ** 0.5) + 1):
    if prime[i] == True:
        j = 2
        while i * j <= n:
            prime[i*j] = False
            j += 1

# 소수 추출
real_prime = [i for i in range(n+1) if prime[i]]

left = right = 0
result = 0
sum_arr = 0

while right <= len(real_prime):
    sum_arr = sum(real_prime[left:right])
    if sum_arr == n:
        result += 1
        right += 1
    elif sum_arr > n:
        left += 1
    else:
        right += 1

print(result)