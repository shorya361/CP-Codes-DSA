import math

k=2
n=int(input())

binary=bin(n)
binary=binary[3:]+binary[2]
binary=int(binary,2)
print(binary-1) # when we are arranging the n from 0 to n-1 ; else answer is binary