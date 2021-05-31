n,m=map(int,input().split())
l=list(map(int,input().split()))
l1=[0]*(n)

for i in range(m):
	p,q=map(int,input().split())
	l1[p-1]+=1
	if q!=n:
		l1[q]-=1
c=0
for i in range(n):
	c+=l1[i]
	l1[i]=c
print(l1)
l1.sort()
l.sort()
a=0
for i in range(n):
	a+=l[i]*l1[i]
print(a)