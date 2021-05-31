def find(nums):
    print(nums)
    print([0,1,2,3,4,5])
    t=nums[0]
    h=nums[0]
    a=-1
    while(True):
        t=nums[t]
        h=nums[nums[h]]
        #print(t, nums[t], h, nums[h])
        if t==h:
            break
    print(nums[nums[t]])
find([1,2,1,3,1,4])