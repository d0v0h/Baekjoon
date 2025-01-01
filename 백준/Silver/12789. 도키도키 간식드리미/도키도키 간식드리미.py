n = int(input())
line = list(map(int, input().split()))

wait_line = []
check = 1

for student in line:
    wait_line.append(student)

    while wait_line and wait_line[-1] == check:
        wait_line.pop()
        check += 1

if len(wait_line) == 0:
    print('Nice')
else:
    print('Sad')