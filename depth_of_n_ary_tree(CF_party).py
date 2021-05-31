from sys import stdin, stdout

parent=[]
total=int(stdin.readline())
for employee in range(total):
    a=int(stdin.readline())
    if a!=-1:
        parent.append(a-1)
    else:
        parent.append(a)
# print(parent)
res=0
depth=[-1 for i in range(total)]
for i in range(total):
    p=i
    current=1
    while(parent[p]!=-1):
        # print(p)
        if depth[p]!=-1:
            current+=depth[p] -1
            break
        current+=1
        p=parent[p]
    if depth[i]==-1:
        depth[i]=current
    res=max(res,current)

print(res)