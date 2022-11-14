#Function to get the just next bigger number than the target  from the array 
def ceiling_num(arr,target):

    start=0
    end=len(arr)-1
    while(start<=end):
        middle=(start+end)//2
        if (target>arr[middle]):
            start=middle+1
        elif (target<arr[middle]):
            end=middle-1
        else:
            return middle
            
    return start
        
#Function call
arr=[2,5,6,8,10,18,20]
result=ceiling_num(arr,11)
print(result)