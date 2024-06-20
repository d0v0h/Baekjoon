import sys, heapq
input = sys.stdin.readline

t = int(input())

arr = []

for i in range(t):
    n = int(input())
    if n != 0:
        heapq.heappush(arr, n)
    else:
        if len(arr) != 0:
            print(heapq.heappop(arr))
        else:
            print(0)