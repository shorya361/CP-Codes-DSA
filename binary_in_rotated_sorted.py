def find(arr,target):
    n=len(arr)
    low=0
    high=n
    while(high>low):
        mid=low+ (high - low)//2
        if arr[mid]==target: #if target is found
            return mid
        am_big=arr[mid]>=arr[0] #if mid value is greater than first element
        target_big=target>=arr[0] # if target value is greater than first element
        # print(mid,am_big,target_big)
        if am_big == target_big: #  both are true then we are in right block of increasing array
            if arr[mid]< target:
                low=mid+1
            else:
                high=mid -1
        else: # else we are in wrong part
            if am_big: # we are in first part and target is in second one
                # print("ye")
                low=mid+1
            else: # we are in second block and target is in first block
                high=mid -1
    return -1

print(find([4,5,6,7,1,2],2))