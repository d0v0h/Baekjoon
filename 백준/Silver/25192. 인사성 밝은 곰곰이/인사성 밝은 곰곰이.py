n = int(input())

result = 0
check = set()
for _ in range(n):
    cmd = input().strip()

    if cmd == 'ENTER':
        result += len(check)
        check = set()
    else:
        check.add(cmd)

print(result + len(check))