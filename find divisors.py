a=int(input())
if a<0:
    print('Wront Input')
else:
    for i in range(1,int(a//2)+1):
        if a%i==0:
            print(i,end=' ')
    print(a)