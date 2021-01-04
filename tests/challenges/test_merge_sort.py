from data_structures_and_algorithms.challenges.merge_sort.merge_sort import mergeSort

def test_insert_sort():
    '''
    input : [8,4,23,42,16,15]
    output : [4, 8, 15, 16, 23, 42]
    '''
    actual = mergeSort([8,4,23,42,16,15])
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected
