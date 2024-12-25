import sys; input = sys.stdin.readline

# 유클리드 호제법을 통해 최대공약수 계산
def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

# 최소공배수 = 두 수의 곱 / 최대공약수
def lcm(a, b):
    return (a * b) / gcd(a, b)

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    print(int(lcm(a, b)))