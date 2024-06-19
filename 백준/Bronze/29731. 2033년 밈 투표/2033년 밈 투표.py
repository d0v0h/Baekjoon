promise = [
    'Never gonna give you up',
    'Never gonna let you down',
    'Never gonna run around and desert you',
    'Never gonna make you cry',
    'Never gonna say goodbye',
    'Never gonna tell a lie and hurt you',
    'Never gonna stop'
]
t = int(input())

check = 0
for i in range(t):
    n = input()
    if n in promise:
        check += 1
    else:
        pass

print('No' if check == t else 'Yes')