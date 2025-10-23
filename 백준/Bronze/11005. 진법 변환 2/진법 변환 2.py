n,b=map(int,input().split())
r='';c=[chr(i) for i in range(97,123)]
while n:
    t=chr(n%b+87)
    if t in c:
        r+=t.upper()
    else:
        r+=str(n%b)
    n //= b
print(r[::-1])