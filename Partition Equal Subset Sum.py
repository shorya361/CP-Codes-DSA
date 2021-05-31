# The question is to check whether the given array can be divided into two subsets of equal sum
def Partition( nums):
        sum_of_arr=sum(nums)
        if sum_of_arr%2!=0:
            return False
        nums.sort()
        aim=sum_of_arr//2
        matrix=[[False for i in range(aim+1)] for j in range(len(nums)+1)]
        n=len(matrix)
        m=len(matrix[0])
        matrix[0][0]=True
        for i in range(n):
            if i > 0:
                for j in range(m):
                    if j==0:
                        matrix[i][j]=True
                    else:
                        if j - nums[i-1] <0:
                            matrix[i][j]= matrix[i-1][j]
                        else:
                            # print(i,j)
                            matrix[i][j] = matrix[i-1][j] or matrix[i-1][j-nums[i-1]]
        for i in matrix:
            print(i)
        return matrix[-1][-1]
Partition([2,2,1,1])

# The approach is to check is the sum of the array is divisible by 2 or not.If it is then there 
# is a possibility else No.
# NOTE: this question is a special case if subset sum (which is a special case of 0/1 Knapsack )
# there are two cases in this as well whether to consider the ith element or not.
# either way that element is going in any of the two subsets. i.e. similar to 0/1 knapsack
# implement an OR operation on both the cases ie. can we get the given sum j with the inclusion
# of ith element or not.
# 
#   matrix[i][j] = matrix[i-1][j] or matrix[i-1][j-nums[i-1]]
#                  not considered      considered
#  anyone of them is True then we can achieve our aim.

#             0  1  2  3 
#      []  0  T  F  F  F
#     [1]  1  T  T  F  F
#   [1,1]  2  T  T  T  F
#  [1,1,2] 3  T  T  T  T
# [1,1,2,2]4  T  T  T  T 
#
