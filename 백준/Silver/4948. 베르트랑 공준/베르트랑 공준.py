import sys; input = sys.stdin.readline
import math

def is_prime(num):
    if num < 2: return 0
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return 0
    return 1

arr = [0]
for i in range(1, 123_456 * 2 + 1):
    check = is_prime(i)
    arr.append(arr[i-1] + check)

n = int(input())

while n != 0:
    print(arr[2 * n] - arr[n])
    n = int(input())