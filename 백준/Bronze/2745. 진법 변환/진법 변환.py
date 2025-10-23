n,b=input().split();n=n.lower();n=n[::-1]
r=0
for i, c in enumerate(n):
    try:
        r += int(c) * (int(b) ** i)
    except:
        r += (ord(c) - 87) * (int(b) ** i)
print(r)