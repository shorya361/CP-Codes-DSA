
from sys import stdin,stdout
n,m,x,y=map(int,stdin.readline().split())
atsame=-1
for i in range(n):
    for j in range(m):
        # if  i<=x and j <=y:
        a=max(x,i)
        b=min(x,i)
        c=max(y,j)
        d=min(y,j)
        stdout.write(str(max((a-b),(c-d)))+ " ")

    stdout.write('\n')
