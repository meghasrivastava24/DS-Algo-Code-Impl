arr=[1,5,8,30,70,90]
target=90

def find_element(arr,target):
    start=0
    end=len(arr)-1
    while(start<=end):
    
        middle=(start+end)//2

        if arr[middle] <target:
            start=middle+1
            print("move right")
        elif arr[middle] >target:
             end=middle-1
             print("move left")
        else:
            print("move there")
            return middle

    return  -1

result=find_element(arr,target)
print(result)