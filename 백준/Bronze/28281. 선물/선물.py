n, x = map(int, input().split())
arr = list(map(int, input().split()))

min_cost = int(1e9)
for i in range(len(arr)-1):
    min_cost = min((arr[i]+arr[i+1]), min_cost)

print(min_cost * x)