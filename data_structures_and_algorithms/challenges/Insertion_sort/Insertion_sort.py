def InsertionSort(arr):

    n = len(arr) # n=6
    for i in range(1,n): # i=1 , range [1,6] || i = 2
        j = i-1 # j=0 | j=1 
        temp = arr[i] # temp = 4 | temp = 23
        while (j >= 0 and temp < arr[j]): # 4 < 8 | 23 < 8 >> false
            arr[j+1] = arr[j] # arr[1] '4' = arr[0] '8'
            j = j-1 # j = -1
        arr[j+1] = temp # arr[0] = 4 | arr[2] = 23
        # [4,8,23,42,16,15]
    return arr

    

print(InsertionSort([8,4,23,42,16,15]))