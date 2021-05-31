
#You are given an integer array coins representing coins of different denominations and 
# an integer amount representing a total amount of money.
#Return the number of combinations that make up that amount. If that amount of money cannot be 
# made up by any combination of the coins, return 0.
#You may assume that you have an infinite number of each kind of coin.



def change( amount, coins) :
        if amount==0:
            return 1
        elif len(coins)==0:
            return -1
        coins.sort()
        matrix=[[0 for i in range(amount+1)] for i in range(len(coins)+1) ]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j==0 and i!=0:
                    matrix[i][j]=1
                else:
                    if coins[i-1] >j:
                        matrix[i][j]=matrix[i-1][j]
                    else:
                        
                        matrix[i][j]= matrix[i-1][j]+ matrix[i][j-coins[max(0,i-1)]]
        return matrix[-1][-1]

print(change(5,[1,2,5]))
#the approach we used here is to make amount of 0 we have only 1 way i.e. no coin included
#but at any other [i][j] , either we select the ith coin or not, if we include ith coin then 
# we have to check for j-ith coin and we do not include the we have to check for [i-1][j]
# add both possibilities for total answer.
#        matrix[i][j] = matrix[i-1][j]   +    matrix[i][j-coins[i-1]]
#                       did not included      included ith coin 
#                       ith coin 
#
# coins 
#   |
#   V  amount -> 0  1  2  3  4  5    
#   0           [0, 0, 0, 0, 0, 0]
#   1           [1, 1, 1, 1, 1, 1]
#   1,2         [1, 1, 2, 2, 3, 3]
#   1,2,5       [1, 1, 2, 2, 3, 4]
