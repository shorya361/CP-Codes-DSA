# PF-Assgn-46

def nearest_palindrome(number):
    num = number
    st = str(number + 1)

    le = len(st)
    a = []

    for i in range(le):
        a.append(int(st[i]))
    st = ""
    if (le % 2 != 0):

        for i in range(le):
            a[le - 1 - i] = a[i]
            st = st + (str(a[i]))
            b = int(st)

        if (b <= (num)):

            st = ""
            b = 0
            a[int(le / 2)] += 1
            for i in range(le):
                st = st + (str(a[i]))
            b = int(st)

            return b
        else:

            return b
    else:
        for i in range(le):
            a[le - 1 - i] = a[i]
            st = st + (str(a[i]))
            b = int(st)
        if (b > (num)):
            return b
        else:
            i = int(le / 2 - 1)
            while (i >= 0):
                if (a[i] != 9):
                    a[i] += 1
                    break
                else:
                    a[i] = 0
                    i -= 1

            st = ""
            b = 0
            for i in range(le):
                a[le - 1 - i] = a[i]
                st = st + (str(a[i]))
                b = int(st)
            return b


number = 121
print(nearest_palindrome(number))