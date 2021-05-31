# You are given an integer array coins representing coins of different denominations and an integer amount representing a
# total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up 
# by any combination of the coins, return -1.
def coinChange( coins, amount):
        
        if amount==0:
            return 0
        coins.sort()
        matrix=[[amount+1 for i in range(amount+1)] for i in range(len(coins)+1) ]
        for i in range(len(matrix)):    
            if i!=0:
                for j in range(len(matrix[0])):
                    if j==0:
                        matrix[i][j]=0
                    else:
                        if j >=coins[i-1]:
                                matrix[i][j] = min(1 + matrix[i][j-coins[i-1]], matrix[i-1][j]) 
                        else:
                            matrix[i][j]=  matrix[i-1][j]
        
        if matrix[-1][-1] ==amount+1:
            return -1
        return matrix[-1][-1]


# In this question, we have to find the minimum number of coins required to get the given amount if we can use infinite no.
# of ith coins. the approach is : we will check that in what scenario we are getting the minimum numbers of coins
# scenario 1: when we include the ith coin:: matrix[i][j-coins[i]] +1 (since we included the ith coin we have to increment
#             the count by 1)
# scenario 2: when we exclude the ith coin:: matrix[i-1][j]
# the answer will be min of both.
# but Note that: we have to initialize the matrix with amount+1 or maxINT at every [i][j] because we are finding minimum
# as well as for the scenarios like amount =3, coins =[2]. 
# Note #2 : the number of coins used to create amount 0 will be 0.

#        amount-> 0    1  2    3  4   5    6   7  8   9   10  11
#   coins        [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
#     1          [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ,11]
#    1,2         [0 , 1 , 1 , 2 , 2 , 3 , 3 , 4 , 4 , 5 , 5 , 6 ]
#   1,2,5        [0 , 1 , 1 , 2 , 2 , 1 , 2 , 2 , 3 , 3 , 2 , 3 ]
