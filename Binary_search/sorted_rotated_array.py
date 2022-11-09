def sum_array(nums):
    
    target=int(input("enter the  sum value"))
    dict={} #value:index
    for index,value in enumerate(nums):
        rem=target-value
        if rem in dict :
            return (dict[rem],index)
        else:
            dict[value]=index
            
    return

nums=[2,5,6,7]
values =sum_array(nums)
print(values)