def binary_search(arr, num): 
    low = 0
    mid = 0
    high = len(arr) - 1

    if type(arr) != list:
        return "invalid input"
    if type(num) != int:
        return "invalid input"
    while low <= high: 
        mid = (high + low) // 2 
        if arr[mid] < num: 
            low = mid + 1
        elif arr[mid] > num: 
            high = mid - 1
        else: 
            return mid
  
    return -1

