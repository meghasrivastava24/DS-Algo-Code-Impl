#Function  to find the element through binary search in a descending order array
arr=[90,70,50,30,1]
target=30

def binary_search_desc_array(arr,target):
    start=0
    end=len(arr)-1
    while(start<=end):
    
        middle=(start+end)//2

        if arr[middle] < target:
            
            end=middle-1

        elif arr[middle] >target:

             start=middle+1
             
        else:
           
            return middle

    return  -1
#Function call
result=binary_search_desc_array(arr,target)
print(result)