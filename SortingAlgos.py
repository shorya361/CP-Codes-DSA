#THis program has all the basic sorting algorithms
#Bubble Sort, Selection Sort, Insertion Sort, Count Sort, Quick Sort, Merge Sort


def BubbleSort(arr):
    for i in range(len(arr)):
        swapped=False
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                swapped=True
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
        if swapped==False:
            return

def SelectionSort(arr):
    for i in range(len(arr)):
        min_id = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_id]:
                min_id=j
        temp=arr[min_id]
        arr[min_id]=arr[i]
        arr[i]=temp

def InsertionSort(arr):
    n=len(arr)
    if n==1:
        return 'only one element'
    for i in range(1,n):
        j=i-1
        exact=i
        while(j>=0):
            if arr[i]<arr[j]:
                exact=j
            j-=1
        ele=arr.pop(i)
        arr.insert(exact,ele)


def CountSort(arr):
    maxelement=max(arr)
    newArr=[0]*(maxelement+1)
    for i in arr:
        newArr[i]+=1
    arr=[]
    for i in range(len(newArr)):
        j=newArr[i]
        while(j>0):
            arr.append(i)
            j-=1
    return arr


def quickSort(arr,start,end):
    if start>=end:
        return
    i=start
    pivot=arr[end]
    j=i
    while(j<end):
        if arr[j]< pivot:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
        j+=1
    arr[i],arr[end]=arr[end],arr[i]
    quickSort(arr,start,i-1)
    quickSort(arr,i+1,end)


def MergeSort(arr,start,end):


    def sort(arr,start,mid,end):
        # print('=================')
        # print(arr[start:mid], arr[mid:end],start,mid,end)
        n=end-start
        newArr=[]
        i=start
        j=mid
        while(i<mid and j<end):
            if arr[i] > arr[j]:
                newArr.append(arr[j])
                j+=1
            elif arr[i]<arr[j]:
                newArr.append(arr[i])
                i+=1
            else:
                newArr.append(arr[i])
                newArr.append(arr[j])
                i+=1
                j+=1
        while(i<mid):
            newArr.append(arr[i])
            i+=1
        while(j<end):
            newArr.append(arr[j])
            j+=1
        for i in range(n):
            arr[i+start]=newArr[i]
        # print(newArr)

    if end-start==1:
        return
    # print(arr[start:end],start,end)
    mid = start + (end-start)//2
    MergeSort(arr,start, mid)
    MergeSort(arr,mid,end)
    sort(arr,start,mid,end)


originalArray=[12,11,53,11,2,21,19,15,11,14]
print(originalArray)

#Bubble Sort o(n*n)
originalArray=[12,11,53,11,2,21,19,15,11,14]
BubbleSort(originalArray)
print(originalArray)

#Selection Sort o(n*n)
originalArray=[12,11,53,11,2,21,19,15,11,14]
SelectionSort(originalArray)
print(originalArray)

#Insertion Sort o(n*n)
originalArray=[12,11,53,11,2,21,19,15,11,14]
InsertionSort(originalArray)
print(originalArray)

#Count Sort o(n+k)
originalArray=[12,11,53,11,2,21,19,15,11,14]
originalArray=CountSort(originalArray)
print(originalArray)

#Quick Sort o(nlogn)
originalArray=[12,11,53,11,2,21,19,15,11,14]
quickSort(originalArray,0,len(originalArray)-1)
print(originalArray)

#Merge Sort o(nlogn)
originalArray=[12,11,53,11,2,21,19,15,11,14]
MergeSort(originalArray,0,len(originalArray))
print(originalArray)



def heapSort(arr,n):

    def heapify(arr,n,i):
        left_child=2*i +1
        right_child=2*i +2
        if left_child < n and right_child<n:
            print('heapify of index ',i, arr ,left_child,right_child)
        else:
            print('heapify of index ',i,arr)
        largest = i
        if left_child <n  and arr[left_child] >arr[largest]:
            largest= left_child 
        if right_child<n and arr[right_child]>arr[largest] :
            largest=right_child
        if largest !=i:
            print('swapping occuring for index ',i, arr[i] , arr[left_child],arr[right_child],'with index',largest,arr[largest])
            arr[i],arr[largest]=arr[largest],arr[i]
            heapify(arr,n,largest)


    # At this  first loop, we are rearranging the array from the parents of the leap node upto to
    # root node, i.e. converting the array into max-heap by making each node greater than its
    # both its left and right child recursively
    for i in range(n//2 -1 , -1,-1):
        heapify(arr,n,i)
    print('------------------')
    
    # After that we are just swapping the largest element node i.e. root node with the last index
    # of array to arrange the array in ascending order. But do remember we are calling heapify
    # method after everyswapping because as the heap is max-heap , the order of heap has been 
    # altered so we have to rearrange that root node again with the maximum element.
    
    for i in range(n-1, 0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)
    print(arr)

array=[4,2,5,7,2,1,3,1,1,1,1]
heapSort(array,len(array))

#Output for understanding
# heapify of index  4 [4, 2, 5, 7, 2, 1, 3, 1, 1, 1, 1] 9 10
# heapify of index  3 [4, 2, 5, 7, 2, 1, 3, 1, 1, 1, 1] 7 8
# heapify of index  2 [4, 2, 5, 7, 2, 1, 3, 1, 1, 1, 1] 5 6
# heapify of index  1 [4, 2, 5, 7, 2, 1, 3, 1, 1, 1, 1] 3 4
# swapping occuring for index  1 2 7 2 with index 3 7
# heapify of index  3 [4, 7, 5, 2, 2, 1, 3, 1, 1, 1, 1] 7 8
# heapify of index  0 [4, 7, 5, 2, 2, 1, 3, 1, 1, 1, 1] 1 2
# swapping occuring for index  0 4 7 5 with index 1 7
# heapify of index  1 [7, 4, 5, 2, 2, 1, 3, 1, 1, 1, 1] 3 4
# ------------------
# heapify of index  0 [1, 4, 5, 2, 2, 1, 3, 1, 1, 1, 7] 1 2
# swapping occuring for index  0 1 4 5 with index 2 5
# heapify of index  2 [5, 4, 1, 2, 2, 1, 3, 1, 1, 1, 7] 5 6
# swapping occuring for index  2 1 1 3 with index 6 3
# heapify of index  6 [5, 4, 3, 2, 2, 1, 1, 1, 1, 1, 7]
# heapify of index  0 [1, 4, 3, 2, 2, 1, 1, 1, 1, 5, 7] 1 2
# swapping occuring for index  0 1 4 3 with index 1 4
# heapify of index  1 [4, 1, 3, 2, 2, 1, 1, 1, 1, 5, 7] 3 4
# swapping occuring for index  1 1 2 2 with index 3 2
# heapify of index  3 [4, 2, 3, 1, 2, 1, 1, 1, 1, 5, 7] 7 8
# heapify of index  0 [1, 2, 3, 1, 2, 1, 1, 1, 4, 5, 7] 1 2
# swapping occuring for index  0 1 2 3 with index 2 3
# heapify of index  2 [3, 2, 1, 1, 2, 1, 1, 1, 4, 5, 7] 5 6
# heapify of index  0 [1, 2, 1, 1, 2, 1, 1, 3, 4, 5, 7] 1 2
# swapping occuring for index  0 1 2 1 with index 1 2
# heapify of index  1 [2, 1, 1, 1, 2, 1, 1, 3, 4, 5, 7] 3 4
# swapping occuring for index  1 1 1 2 with index 4 2
# heapify of index  4 [2, 2, 1, 1, 1, 1, 1, 3, 4, 5, 7]
# heapify of index  0 [1, 2, 1, 1, 1, 1, 2, 3, 4, 5, 7] 1 2
# swapping occuring for index  0 1 2 1 with index 1 2
# heapify of index  1 [2, 1, 1, 1, 1, 1, 2, 3, 4, 5, 7] 3 4
# heapify of index  0 [1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 7] 1 2
# heapify of index  0 [1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 7] 1 2
# heapify of index  0 [1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 7] 1 2
# heapify of index  0 [1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 7]
# heapify of index  0 [1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 7]
# [1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 7]