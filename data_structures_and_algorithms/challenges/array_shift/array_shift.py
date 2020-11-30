def insertShiftArray(arr,num):
    if type(arr) != list:
        return 'invalid input'
    if type(num) != int:
        return 'TypeError! should be an int'
    midpoint = len(arr)//2+1
    if len(arr)%2 == 0:
      
        x = arr[:len(arr)//2] + [num] + arr[len(arr)//2:]
        return x
    else:
        x = arr[0:midpoint] + [num] + arr[midpoint:]
        return (x)

