n,m=map(int,input().split())
a=list(map(int,input().split()));max_m=0

for i in range(len(a)-2):
    for j in range(i+1,len(a)-1):
        for k in range(j+1,len(a)):
            temp = a[i] + a[j] + a[k]
            if max_m < temp <= m:
                max_m = temp
print(max_m)