def recursion(str, s, e):
    global cnt
    cnt += 1
    if s >= e:
        return 1
    elif str[s] != str[e]:
        return 0
    else:
        return recursion(str, s+1, e-1)

def isPalindrome(str):
    return recursion(str, 0, len(str)-1)

n = int(input())

for _ in range(n):
    str = input()
    cnt = 0
    print(isPalindrome(str), cnt)