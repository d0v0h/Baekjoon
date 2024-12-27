# 1. 분모를 최소공배수로 만듦
# 2. 최소공배수가 된 분모를 기준으로 분자 갱신
# 3. 기약분수로 표현 (분모와 분자를 gcd하여 나눔)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

a, b = map(int, input().split())
c, d = map(int, input().split())

deno = lcm(b, d)
nume = (a * (deno // b) + c * (deno // d))

modul = gcd(deno, nume)
print(nume // modul, deno // modul)