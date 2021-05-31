#PF-Assgn-42
def find_factors(num):
    print("find factors:",num)                                                    #3
    #Accepts a number and returns the list of all the factors of a given number
    factors = []
    for i in range(2,(num+1)):
        if(num%i==0):
            factors.append(i)
    return factors

def is_prime(num, i):                                                   #5
    #Accepts the number num and num/2 --> i and returns True if the number is prime ,else returns False
    if(i==1):
        return True
    elif(num%i==0):
        return False
    else:
        return(is_prime(num,i-1))

def find_largest_prime_factor(list_of_factors):
    le={}
    list_of_factors.sort()
    le=list_of_factors
    n=len(le)
    print("length of list of factors",le)
    max=le[n-1]
    return max
    #Accepts the list of factors and returns the largest prime factor

def find_f(num):
    list=[]
    list=find_factors(num)                                                        #2
    print("list of factors",list)
    list_prime=[]
    for i in list:#Accepts the number and returns the largest prime factor of the number
        if(is_prime(i,i/2)):                                                      #4
            list_prime.append(i)
    print("list_prime",list_prime)
    return find_largest_prime_factor(list_prime)

def find_g(num):
    sum=0
    n=8
    while(n):
        sum=sum+find_f(num+n)                                                      #1
        n-=1
    return sum
    #Accepts the number and returns the sum of the largest prime factors of the 9 consecutive numbers starting from the given number

#Note: Invoke function(s) from other function(s), wherever applicable.

print(find_g(10))