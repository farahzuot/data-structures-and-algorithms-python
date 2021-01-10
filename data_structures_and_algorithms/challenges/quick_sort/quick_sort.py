def quickSort(arr, left, right): 
    if left < right: # 0 < 5 || 0 < 1 || 3 < 5
        # print(left,right)
        pivot = partition(arr, left, right) 
        # print (arr)
        # pivot = partition([8,4,23,42,16,15], 0, 5) >> 2. [8,4,15,42,16,23]
        # || pivot = partition([8,4,15,42,16,23], 0, 1) >> 0. [4,8,15,42,16,23]
        # || pivot = partition([4,8,15,42,16,23], 3, 5) >> 4. [4,8,15,16,23,42]
        # || pivot = partition([4,8,15,16,23,42], 4, 5) >> 5. [4,8,15,16,23,42]
        # print(left, pivot-1)
        quickSort(arr, left, pivot-1)
        # quickSort([8,4,23,42,16,15], 0, pivot-1) 
        # || ([8,4,15,42,16,23], 0, 1)
        # || ([4,8,15,42,16,23], 0, -1) break if statement.
        quickSort(arr, pivot+1, right)
        # quickSort([4,8,15,42,16,23], 1, 1) break if statement. >> back to right =5 and pivot =2.
        # || ([4,8,15,42,16,23], 3, 5)
        # || ([4,8,15,42,16,23], 4, 5)
    return arr


def partition(arr, left, right): 
    i = (left-1) # i = -1 \\\ i = -1 \\\ i = 2
    pivot = arr[right] # pivot=15 \\\ pivot=4 \\\ pivot=23
    for j in range(left, right): #(0,5), j=0 || j=1 || j=2 \\\  (0,1),, j =0 \\\ (3,5),, j=3 || j=4
        if arr[j] <= pivot: # 8 <= 15 ? T || 4 <= 15? T || 23 <= 15 ? F \\\ 8 <= 4 ? F \\\ 42 < 23 ? F|| 16<23?T
            i = i+1 # i = 0, i=1 \\\ i=0 \\\ i=3
            # print(arr[i], arr[j])
            arr[i], arr[j] = arr[j], arr[i] # arr[0]=8,, arr[0]=8 || arr[1]=4,, arr[1]=4 \\\ arr[3]=16,, arr[4]=42
    arr[i+1], arr[right] = arr[right], arr[i+1] # arr[2]=15,, arr[5]=23 \\\ arr[0]=4,, arr[1]=8 \\\ arr[4]=23,, arr[5] =42
    return (i+1) # 2. > [8,4,15,42,16,23] \\\ 0. > [4,8,15,42,16,23] \\\ 4. [4,8,15,16,23,42]
    

if __name__ == "__main__":
    arr = [8,4,23,42,16,15]
    print(quickSort(arr, 0, len(arr)-1) )
