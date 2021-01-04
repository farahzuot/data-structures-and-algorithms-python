def mergeSort(arr):
    n = len(arr) # n=6
    if n > 1:
        mid = n//2 # mid=3
        left = arr[0:int(mid)] # left=[8,4,23]
        right = arr[int(mid):n] # right=[42,16,15]
        mergeSort(left) # left >> left,right > [8], [4,23]
        mergeSort(right) # right >> left,right > [4],[23]
        # print(left,right,arr)
        merge(left,right,arr) # merge([4],[23],[4,23]) ||| [8] [4, 23] [8, 4, 23]
    return arr

def merge(left,right,arr):
    i =0
    j =0
    k =0
    while (i < len(left) and j < len(right)): # 0 < 1 && 0 < 1 ||| 0 < 1 && 0 < 2 ||| 0 < 1 && 1 < 2
        if left[i] <= right[j]: # 4 <= 23 > true ||| 8 <= 4 > false ||| 8 <= 23 > true
            arr[k] = left[i] # arr[0] = 4 || arr[1] = 8
            i = i + 1 # i=1 ||| i = 1
        else:
            arr[k] = right[j] # arr[0] = 4
            j=j+1 # j = 1
        k = k+1 # k = 1 ||| k = 1 ||| k = 2

    if i == len(left): # 1 == 1 > true ||| 1 == 1 
        arr[k] = right[j] # arr[1] = 23 ||| arr[2] = 23
    else:
        arr[k] = left[i] 
    # print(arr)
    # [4,23]
    # [4,8,23]

if __name__ == "__main__":
    print(mergeSort([8,4,23,42,16,15]))


