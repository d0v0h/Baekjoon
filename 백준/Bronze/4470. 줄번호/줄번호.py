n = int(input())

string = []
for _ in range(n):
    string.append(input())

for i, s in enumerate(string):
    print(str(i+1) + '. ' + s)
