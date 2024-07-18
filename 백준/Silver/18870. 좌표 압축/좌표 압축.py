import sys
input = sys.stdin.readline

n = int(input())

cnt = {}

arr = list(map(int, input().split()))
arr_copy = arr.copy()
arr.sort()
i = 0
for num in arr:
    if num not in cnt.keys():
        cnt[num] = i
        i += 1

for num in arr_copy:
    print(cnt[num], end=' ')