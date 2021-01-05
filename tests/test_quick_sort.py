from data_structures_and_algorithms.challenges.quick_sort.quick_sort import quickSort

def test_insert_sort():
    arr = [8,4,23,42,16,15]
    actual = quickSort(arr, 0, len(arr)-1)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected

def test_reversed_list_sort():
    arr = [20,18,12,8,5,-2]
    actual = quickSort(arr, 0, len(arr)-1)
    expected = [-2,5,8,12,18,20]
    assert actual == expected

def test_Few_uniques_sort():
    arr = [5,12,7,5,5,7]
    actual = quickSort(arr, 0, len(arr)-1)
    expected = [5,5,5,7,7,12]
    assert actual == expected

def test_Nearly_sorted_sort():
    arr = [2,3,5,7,13,11]
    actual = quickSort(arr, 0, len(arr)-1)
    expected = [2,3,5,7,11,13]
    assert actual == expected