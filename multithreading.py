#PF-Tryout
from threading import Thread
def func1():
    result_sum=0
    for i in range(10000001):#Write the code to find the sum of numbers from 1 to 10000000
        result_sum+=i
    print("Sum from func1:",result_sum)

def func2():
    result_sum=0
    for i in range(5):
        p=int(input())
        result_sum+=p
    #Write the code to accept 5 numbers from user and find its sum
    print("Sum from func2:",result_sum)

#Modify the code given below to execute func1() and func2() in two separate threads
thread1=Thread(target=func1())
thread1.start()
thread2=Thread(target=func2())
thread2.start()                                 #starts the thread

thread1.join()
print("hello")
thread2.join()
print("damn")