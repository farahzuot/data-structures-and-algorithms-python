from data_structures_and_algorithms.challenges.ll_zip.ll_zip import zipLists

def test_happy_path():
    '''
    this function will test the normal path
    '''
    actual = zipLists([1,2,3],[1,2,3])
    expected = [1,1,2,2,3,3]
    assert actual == expected

def test_invilid_input():
    '''
    this function will test if the inputs are not lists
    '''
    actual = zipLists(1,[1,2,3])
    expected = "invalid input"
    assert actual == expected

def test_listTwo_longer_than_listOne():
    '''
    this function will test if the second list longer than the first list
    '''
    actual = zipLists([1,2,3],[1,2,3,4,5])
    expected = [1,1,2,2,3,3,4,5]
    assert actual == expected

def test_listOne_longer_than_listTwo():
    '''
    this function will test if the first list longer than the second list
    '''
    actual = zipLists([1,2,3,4,5],[1,2,3])
    expected = [1,1,2,2,3,3,4,5]
    assert actual == expected