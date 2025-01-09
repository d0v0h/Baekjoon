t = int(input())

arr = [0] * 10001
for i in range(t):
    arr[i] = int(input())

check = [0] * 10001
check[0] = arr[0]
check[1] = arr[0] + arr[1]
check[2] = max(arr[0] + arr[2], arr[1] + arr[2], check[1])
for i in range(3, t):
    check[i] = max(arr[i] + arr[i-1] + check[i-3], arr[i] + check[i-2], check[i-1])

print(max(check))