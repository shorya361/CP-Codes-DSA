def longest_palindromic_subsequence(STR):
    first=STR
    second=STR[::-1]
    matrix=[[0 for i in range(len(first)+1)] for j in range(len(second)+1)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i!=0 and j!=0:
                if first[j-1]==second[i-1]:
                    matrix[i][j]= 1 + matrix[i-1][j-1]
                else:
                    matrix[i][j]= max(matrix[i-1][j],matrix[i][j-1])
    for i in matrix:
        print(i)
    i=len(matrix)-1
    j=len(matrix[0])-1
    res=''
    while(i >=0  and j>=0):
            if matrix[i][j]> matrix[i][j-1] and matrix[i][j]> matrix[i-1][j]:
                i-=1
                j-=1
                res=first[j]+res
            elif matrix[i][j] == matrix[i-1][j]:
                i-=1
            elif matrix[i][j] == matrix[i][j-1]:
                j-=1
    print(res)

longest_palindromic_subsequence('ABDBCA')