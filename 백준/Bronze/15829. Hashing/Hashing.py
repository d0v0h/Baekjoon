import sys
input = sys.stdin.readline

l = int(input())

alpha = {chr(i): i-96 for i in range(97,123)}
string = input().strip()

power_31 = [1]
for i in range(1, l):
    power_31.append(power_31[i-1] * 31)

result = 0
for i, char in enumerate(string):
    result += alpha[char] * power_31[i]

print(result % 1234567891)