from data_structures_and_algorithms.challenges.array_binary_search.array_binary_search import binary_search

"""
tests : 
the type of list, num are correct
the index of number if its on the left side
the index of number if its on the right side
the index of number if its on the middle
"""


# def test_list_type():
#     actual = binary_search(5,4)
#     expected = "invalid input"
#     assert actual == expected

def test_num_type():
    actual = binary_search([1,2,3],'3')
    expected = "invalid input"
    assert actual == expected

def test_num_left_side():
    actual = binary_search([1,2,3,4,5],2)
    expected = 1
    assert actual == expected

def test_num_right_side():
    actual = binary_search([1,2,3,4,5],5)
    expected = 4
    assert actual == expected

def test_num_middle():
    actual = binary_search([1,2,3,4,5],3)
    expected = 2
    assert actual == expected


