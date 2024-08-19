import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())

queue = []
for _ in range(n):
    w, v = map(int, input().split())
    heapq.heappush(queue, (w, -v))

bags = []
for _ in range(k):
    c = int(input())
    bags.append(c)
bags.sort()

socet = []
result = 0
# 작은 무게의 가방에 가치있는 보석을 넣는 방법 선택
for bag in bags:
    while queue and queue[0][0] <= bag:
        w, v = heapq.heappop(queue)
        heapq.heappush(socet, v)

    if len(socet) != 0:
        result += -heapq.heappop(socet)

print(result)