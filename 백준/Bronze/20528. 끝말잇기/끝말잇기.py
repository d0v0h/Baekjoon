import sys; input = sys.stdin.readline

n = int(input())

string = list(input().split())

temp = ''
for i, str in enumerate(string):
    if str != str[::-1]:
        print(0)
        break
    if i != 0:
        if temp != str[0]:
            print(0)
            break
    else:
        temp = str[0]
else:
    print(1)