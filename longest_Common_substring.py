def longest_common_substring(first, second):
    matrix=[[0 for i in range(len(second)+1)] for i in range(len(first)+1)]
    final_index=None
    longest_length=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i!=0 and j!=0:
                if first[i-1] == second[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]+1
                    if matrix[i][j] > longest_length:
                        final_index=i
                        longest_length= matrix[i][j]
    for i in matrix:
        print(i)
    # print(final_index, longest_length)
    for i in range(final_index - longest_length, final_index):
        print(first[i],end="")
    return 
longest_common_substring("PPSSPRT",'PASSPORT')

#output SSP