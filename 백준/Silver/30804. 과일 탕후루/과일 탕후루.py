import sys
input = sys.stdin.readline

n = int(input())
fruit = list(map(int, input().split()))

count = [0] * n
kind = []
st, end = 0, 0

while end != n:
    if fruit[end] not in kind:
        kind.append(fruit[end])

    if len(kind) > 2:
        for check in range(end-1, -1, -1):
            if fruit[end-1] != fruit[check]:
                kind.remove(fruit[check])
                st = check + 1
                break
    count[end] = end - st + 1
    end += 1
print(max(count))