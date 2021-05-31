
from sys import stdin,stdout
n=int(stdin.readline())
arr=list(map(int,input().split()))
arr.sort()
arr=arr[-6:]
# print(arr)
a=arr[0]
b=arr[-4]
c=arr[-1]
d=arr[-2]
e=arr[-3]
f=arr[1]
x= a+ 4*b + 6*c + 4*d + e
y= b+ 4*c + 6*d + 4*e + f
print(x * y)

