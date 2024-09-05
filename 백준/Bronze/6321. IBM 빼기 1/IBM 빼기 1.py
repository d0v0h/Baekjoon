t = int(input())

result = []
for _ in range(t):
    temp = ''
    string = input()

    for s in string:
        if s == 'Z':
            temp += 'A'
        else:
            temp += chr(ord(s)+1)

    result.append(temp)

for i, r in enumerate(result):
    print(f'String #{i+1}')
    print(r)
    print()