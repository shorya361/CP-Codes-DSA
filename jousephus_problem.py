def josephus(n,k):
    if n==1:
        return 0
    return (josephus(n-1,k)+k)%n
print(josephus(41,2)) # starting number is 0 