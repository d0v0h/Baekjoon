s=input().upper()
a={w:s.count(w) for w in set(s)}
r=[k for k,v in a.items() if max(a.values()) == v]
print('?') if len(r) > 1 else print(r[0])