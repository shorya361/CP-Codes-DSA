def findBinary(matrix,n):
    if len(matrix)==0:
        return False
    row_len=len(matrix)
    col_len=len(matrix[0])

    low =0
    high = row_len*col_len
    mid = (low + high) // 2
    while(low<high):
        mid=(low+high)//2

        if matrix[mid//col_len][mid%col_len] ==n:
            return True
        elif matrix[mid//col_len][mid%col_len] < n:
            low =mid +1
        else:
            high = mid

    return False


mat=[
     [1,2,3,4],
     [5,6,7,8],
     [9,11,21,33]
    ]

print(findBinary(mat,21))
# row=3
# col=4
# low =0
# high=7
# mid=3
# mat[ ][ ]==8
#
