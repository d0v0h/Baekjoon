t = int(input())

result = [['.' for _ in range(20)] for _ in range(10)]

for _ in range(t):
    cmd = input()
    row = ord(cmd[0])
    col = int(cmd[1:])

    result[row-65][col-1] = 'o'

for r in result:
    print(*r, sep='')