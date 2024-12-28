import sys; input = sys.stdin.readline
import math

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def search_prime(n):
    while True:
        if is_prime(n):
            return n
        n += 1


t = int(input())

for _ in range(t):
    num = int(input())
    print(search_prime(num))