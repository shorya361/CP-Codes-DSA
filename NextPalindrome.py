def findnextPalindrome(n):
    number=str(n)
    if n<9:
        return n+1
    elif n +1 == (10 ** len(number)):
        return n+2
    if len(number)%2==0:
        firstHalf=(number[:len(number)//2])
        secondHalf=number[len(number)//2:]
        if int(secondHalf) >= int(firstHalf[::-1]):
            firstHalf=int(firstHalf) +1
            firstHalf=str(firstHalf)
            number = firstHalf + firstHalf[::-1]
        else:
            number=firstHalf+firstHalf[::-1]

    else:
        firstHalf = (number[:len(number) // 2 +1 ])
        first=number[:len(number) // 2]
        middle=firstHalf[-1]
        secondHalf = number[len(number) // 2 +1:]
        if int(first[::-1]) > int(secondHalf):
            number=first + middle + first[::-1]

        else:
            firstHalf=int(firstHalf)+1
            firstHalf=str(firstHalf)
            first=firstHalf[:len(firstHalf)-1]
            middle=firstHalf[-1]
            number=first+ middle + first[::-1]
    return number
print(findnextPalindrome(9999))