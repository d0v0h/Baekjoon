r=[[0 for _ in range(100)] for _ in range(100)];cnt=0
n=int(input())
for _ in range(n):
    x,y=map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            if r[i][j] == 0:
                r[i][j] = 1
                cnt += 1
print(cnt)