n = int(input())
tax = list(map(int, input().split()))
cost = int(input())

s, e = 0, max(tax)
while s <= e:
    mid = (s+e) // 2
    total = 0
    for t in tax:
        total += min(mid, t)
    
    if total > cost:
        e = mid - 1
    else:
        s = mid + 1

print(e)