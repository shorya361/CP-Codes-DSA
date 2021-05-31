sentence="the world is here at sharda university"
print(sentence)
a=[]
a=sentence.split()
b=""
for i in range(len(a)):
    if(i!=0):
        b+=" "
    if(i%2==0):
        le=len(a[i])
        c=[]
        for j in range(le):
            c.append(a[i][j])

        for j in range(int(le/2)):

            temp=c[j]
            c[j]=c[le-1-j]
            c[le-j-1]=temp

        for i in c:
            b+=i


    else:
        le=len(a[i])
        vowels=[]
        cons=[]
        for j in range(le):
            if(a[i][j]=="a" or a[i][j]=="e" or a[i][j]=="u" or a[i][j]=="i" or a[i][j]=="o"):
                vowels.append(a[i][j])
            else:
                cons.append(a[i][j])
        for j in range(len(cons)):
            b+=cons[j]
        for j in range(len(vowels)):
            b+=vowels[j]



return b
