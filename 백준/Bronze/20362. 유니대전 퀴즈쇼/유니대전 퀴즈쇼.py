import sys; input = sys.stdin.readline

n, s = input().split()

arr = {}
for _ in range(int(n)):
    name, answer = input().split()

    arr[name] = answer

key = ''
answer = arr[s]
result = 0

for key, val in arr.items():
    if key == s:
        break

    if answer == val:
        result += 1

print(result)