x=int(input())
for i in range(int(input())):
    a,b=map(int,input().split())
    x-=a*b
print('Yes') if x == 0 else print('No')