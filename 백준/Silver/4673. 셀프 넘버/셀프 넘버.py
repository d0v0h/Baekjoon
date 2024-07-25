arr = [i for i in range(10001)]
answer = set()

for num in arr:
    checks = str(num)
    for check in checks:
        num += int(check)
    if num <= 10000:
        answer.add(num)

for check in answer:
    arr[check] = 0

for num in arr:
    if arr[num] != 0:
        print(num)