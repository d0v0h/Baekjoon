import math
a,b,v=map(int,input().split());cnt=1;o=a
d=v-a;m=a-b
print(math.ceil(d/m)+1)