import sys
input = sys.stdin.readline

l = int(input())

alpha = {chr(i): i-96 for i in range(97,123)}
string = input().strip()

result = 0
for i, char in enumerate(string):
    result += alpha[char] * 31 ** i

print(result)