import sys
input = sys.stdin.readline

def checkFizzBuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0 and num % 5 != 0:
        return 'Fizz'
    elif num % 3 != 0 and num % 5 == 0:
        return 'Buzz'
    else:
        return num

arr = []
for _ in range(3):
    try:
        value = input().strip()
        arr.append(int(value))
    except ValueError:
        arr.append(value)

idx = num = 0
for i, val in enumerate(arr):
    if type(val) == int:
        idx = i
        num = val
        break

if i == 0:
    num += 3
elif i == 1:
    num += 2
else:
    num += 1

print(checkFizzBuzz(num))