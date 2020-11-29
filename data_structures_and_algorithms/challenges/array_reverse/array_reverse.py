def reverse_array(arr):
    """Reverses a list
    Args:
        arr (list): python list

    Returns:
        [list]: list in reversed form
    """
    # put your function implementation here
    i = len(arr) - 1 
    result=[]
    while i >= 0 :
        result.append(arr[i])
        i -= 1
    print(result)
    return result

reverse_array([89, 2354, 3546, 23, 10, -923, 823, -12])