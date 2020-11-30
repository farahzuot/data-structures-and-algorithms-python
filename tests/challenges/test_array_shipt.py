from data_structures_and_algorithms.challenges.array_shift.array_shift import insertShiftArray

"""
type of list
type of num
add a number to odd list
add a number to even list

"""

def test_list_type():
    actual = insertShiftArray(5,4)
    expected = 'invalid input'
    assert actual == expected

def test_num_type():
    actual = insertShiftArray([1,2,3],'3')
    expected = 'TypeError! should be an int'
    assert actual == expected

def test_add_even():
    actual = insertShiftArray([4,6,8,12],10)
    expected = [4,6,10,8,12]
    assert actual == expected

def test_add_odd():
    actual = insertShiftArray([13,6,5,4,2],10)
    expected =[13,6,5,10,4,2]
    assert actual == expected