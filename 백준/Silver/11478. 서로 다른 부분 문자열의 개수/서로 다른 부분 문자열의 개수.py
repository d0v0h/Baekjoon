import sys; input = sys.stdin.readline

string = input().strip()

check = {}

for i in range(1, len(string)+1):
    for j in range(len(string)):
        if len(string[j:j+i]) == i:
            check[string[j:j+i]] = 1

print(len(check))