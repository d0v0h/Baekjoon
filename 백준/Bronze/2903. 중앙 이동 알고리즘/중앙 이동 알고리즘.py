r=[2]
for i in range(1,16):
    r.append(r[i-1]+r[i-1]-1)
print(r[int(input())]**2)