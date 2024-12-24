import sys; input = sys.stdin.readline

string = input().strip()

check = set()

for i in range(1, len(string)+1):
    for j in range(len(string)):
        check.add(string[j:j+i])

print(len(check))