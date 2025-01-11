import sys; input = sys.stdin.readline

string = input().strip()

check = [[0 for i in range(26)] for _ in range(len(string))]

# 가장 먼저 등장한 문자열 등록
check[0][ord(string[0]) - 97] = 1
for i in range(1, len(string)):
    check[i] = check[i-1].copy()
    check[i][ord(string[i]) - 97] += 1

n = int(input())
# 구간 내 문자 찾기
for _ in range(n):
    result = 0
    a, l, r = input().split()
    l, r = int(l), int(r)

    if l == 0:
        print(check[r][ord(a) - 97])
    else:
        print(check[r][ord(a) - 97] - check[l - 1][ord(a) - 97])