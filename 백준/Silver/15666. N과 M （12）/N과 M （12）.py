import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = []
temp = []

def sol(start):
    if len(temp) == m:
        if temp not in result:
            result.append(temp[:])
        return

    for i in range(start, n):
        num = arr[i]
        temp.append(num)
        sol(i)
        temp.pop()

sol(0)
for r in result:
    print(*r)