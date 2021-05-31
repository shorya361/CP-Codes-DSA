# PF-Assgn-41
def find_ten_substring(num_str):
    list = []
    for i in range(len(num_str) - 1):
        j = i + 1
        sum =int(num_str[i])
        while (j != len(num_str)):
            print(num_str[i:j + 1])
            sum = sum + int(num_str[j])
            if (sum == 10):
                list.append(num_str[i:j+1])
                print("hi",num_str[i:j+1 ])
                j += 1
            elif (sum > 10):
                sum=0
                break
            else:
                j += 1

    return list

    # Remove pass and write your logic here


num_str = '910343145'
print("The number is:", num_str)
result_list = find_ten_substring(num_str)
print(result_list)
