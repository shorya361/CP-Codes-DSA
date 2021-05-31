from sys import stdin,stdout
elements=[6,28]
for i in range(2,14+1):
    elements.append(2*elements[i-1] - elements[i-2] + 16)
print(elements)
k=0
for testcases in range(int(stdin.readline())):
    n=int(stdin.readline())
    for i in range(1,n+1):
        print(" "*(n-i)*3,end="")
        for i in range(i):
            print(format(elements[k],'05'),end=" ")
            k+=1
        print()
