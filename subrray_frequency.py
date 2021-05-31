
from collections import defaultdict as dict
from bisect import bisect_left as lower_bound
from bisect import bisect_right as upper_bound
store = dict(list)
# Returns frequency of element
# in arr[left-1..right-1]
def findFrequency(arr, n, left, right, element):
    # Find the position of
    # first occurrence of element
    a = lower_bound(store[element], left)
    # Find the position of
    # last occurrence of element
    b = upper_bound(store[element], right)
    print(a,b)
    return b - a

arr = [2, 8, 6, 9, 8, 6, 8, 2, 11]
n = len(arr)

# Storing the indexes of
# an element in the map
for i in range(n):
    store[arr[i]].append(i + 1)

print(store)
# Prfrequency of 2 from position 1 to 6
print("Frequency of 2 from 1 to 6 = ",
      findFrequency(arr, n, 1, 2, 6))


# This code is contributed by Mohit Kumar
