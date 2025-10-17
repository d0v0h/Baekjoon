n=int(input());s=list(map(int,input().split()))
h=max(s);s=[i/h*100 for i in s]
print(sum(s)/len(s))