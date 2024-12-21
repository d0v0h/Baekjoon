import sys; input = sys.stdin.readline

n, m = map(int, input().split())

arr = {}
for _ in range(n):
    string = input().strip()
    arr[string] = 0

for _ in range(m):
    search = input().strip()
    if search in arr.keys():
        arr[search] += 1

result = 0
for key, val in arr.items():
    result += val

print(result)