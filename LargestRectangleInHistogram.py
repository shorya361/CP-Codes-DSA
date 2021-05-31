def findLargestRectangle(arr):
    posi=0
    maxArea=-1
    positions=[]
    values=[]
    index=0
    n=len(arr)
    while(index<n):
        if len(values)==0 or arr[index]> values[-1]:
            positions.append(index)
            values.append(arr[index])
        elif arr[index] < values[-1]:
            poppedpositions = 0
            while(len(values)>0 and arr[index]<values[-1]):
                poppedpositions=positions.pop()
                value=values.pop()
                area=value * (index-poppedpositions)
                maxArea=max(maxArea,area)
            positions.append(poppedpositions)
            values.append(arr[index])
        print(positions,values,maxArea,index)
        index+=1
    while(len(positions)>0):
        poppedpositions=positions.pop()
        value=values.pop()
        area=value *(index - poppedpositions)
        maxArea=max(maxArea,area)
    return maxArea

print(findLargestRectangle([6,2,5,4,5,1,6]))