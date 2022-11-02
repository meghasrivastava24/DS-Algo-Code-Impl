arr=[
    [2,4,5],
    [3,6,89],
    [88,90,20]
]
def max_2d_array(array_1):
    max=array_1[0][0]
    for i in range(len(array_1)):
        for j in range(len(array_1[i])):
            if max<array_1[i][j]:
                max=array_1[i][j]

    return max


result=max_2d_array(arr)
print(result)

