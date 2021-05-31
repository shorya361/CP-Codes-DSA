#------------------------------------------------------------------------------------------------
#author : Shorya
#contact: shorya361@gmail.com
#Punk_GTS python Template
from sys import stdin,stdout
from collections import  Counter, defaultdict
import  math
def readInt(): return int(stdin.readline())
def readString(): return (stdin.readline())[:-1]
def readListInt(): return list(map(int,stdin.readline().split()))
def readListStr(): return list(map(str,stdin.readline().split()))
def nextLine(): stdout.write("\n")
def show(x): stdout.write(str(x) +"\n")
def showInline(x) : stdout.write(str(x)+" ")
def showList(x):
    for i in x:
        stdout.write(str(i)+" ")
    nextLine()
def show2D(x):
    for i in range(len(x)):
        for j in range(len(x[0])):
            stdout.write(str(x[i][j])+" ")
        nextLine()
def emptyList(length , value=-1): return [value]*length
def empty2D(row , col , val=-1) : return [ [val for i in range(col)] for j in range(row) ]
def isSquare(x):
    if ((x**(0.5))*10) % 10 ==0:
        return 1
    return 0
def isLog(val,base):
    a=math.log(val,base)
    if (a*10 )%10==0:
        return 1
    else:
        return 0
def showDict(dic):
    for i in dic:
        print(i," =>  ",dic[i])
def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
        prime[0]==prime[1]==False
    return prime
#-------------------------------------------------------------------------------------------------
primes=SieveOfEratosthenes(100000)
# print(primes)
def solve():
        #start coding
        for testcases in range(readInt()):
            num=readListInt()
            n1=num[0]
            n2=num[1]
            num=[]
            for i in range(n1,n2+1):
                if primes[i]==True:
                    num.append(i)
            # showList(num)
            newnum=[]
            for i in range(len(num)):
                for j in range(len(num)):
                        a=str(num[i])+str(num[j])
                        if primes[int(a)]==True:
                            newnum.append(int(a))

            a=min(newnum)
            b=max(newnum)
            newnum=set(newnum)
            # show(len(newnum))
            # showList(newnum)
            # showInline(a)
            # showInline(b)
            # show(len(newnum))
            for i in range(len(newnum)-2):

                c=a+b
                a=b
                b=c
                # showInline(c)
            # print()
            show(c)
solve()