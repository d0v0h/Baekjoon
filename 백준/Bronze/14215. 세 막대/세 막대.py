dist = list(map(int, input().split()))
max_d = max(dist)
dist.remove(max_d)

if max_d >= sum(dist):
    print(sum(dist) * 2 - 1)
else:
    print(sum(dist) + max_d)