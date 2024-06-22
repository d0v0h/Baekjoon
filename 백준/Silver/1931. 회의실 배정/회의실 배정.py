import sys
input = sys.stdin.readline

t = int(input())

arr = []

for i in range(t):
    s, e = map(int, input().split())
    arr.append([s, e])

arr.sort(key=lambda x : (x[1], x[0]))

start = end = count = 0
for s, e in arr:
    if s >= end:
        count += 1
        end = e

print(count)