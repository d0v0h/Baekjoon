import sys
input = sys.stdin.readline

arr = []
for _ in range(5):
    arr.append(int(input()))

arr.sort()
print(sum(arr)//(len(arr)))
print(arr[2])