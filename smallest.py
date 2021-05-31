num=16
n=1
while(1):
    count=1
    for i in range(1,int(n/2)+1):
        if(n%i==0):
            count+=1
    if(count==num):
        print(n)
        break
    else:
        n+=1