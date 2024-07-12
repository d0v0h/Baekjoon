import sys
input = sys.stdin.readline

n = int(input())
s = int(input())
m = input().strip()

pn = 'IOI'

for i in range(1, n):
    pn += 'OI'

length = len(pn)
count = 0
for i in range(s-length+1):
    if m[i:i+length] == pn:
        count += 1

print(count)