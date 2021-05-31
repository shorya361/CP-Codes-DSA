# PF-Assgn-57
def check_prime(number):
    for i in range(2, int(number / 2)+1):  # remove pass and write your logic here. if the number is prime return true, else return false
        if (number % i == 0):
            return False
    return True


def rotations(num):
    st = str(num)
    length = len(st)
    count = length
    list_of_combination = [num]
    if (length == 1):
        return list_of_combination
    while (count - 1):
        msb = int(num / (10 ** (length - 1)))
        lsb = int(num % (10 ** (length - 1)))
        number = lsb * 10 + msb
        if (number != num):
            num = number

            list_of_combination.append(number)
        count -= 1
    return list_of_combination

            # remove pass and write your logic here. It should return the list of different combinations of digits of the given number.


# Rotation should be done in clockwise direction. For example, if the given number is 197, the list returned should be [197, 971, 719]

def get_circular_prime_count(limit):
    count=0
    for i in range(2,limit):
        lst=rotations(i)
        c=0
        for j in lst:
            if(check_prime(j)):
                c+=1
            else:

                break
        if(c==len(lst)):
            print(i,lst)

            count+=1
    return count


# remove pass and write your logic here.It should return the count of circular prime numbers below the given limit.

# Provide different values for limit and test your program
print(get_circular_prime_count(500))
