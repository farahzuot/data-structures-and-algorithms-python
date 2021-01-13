from data_structures_and_algorithms.challenges.left_join.left_join import Hashtable,left_join

def test_left_join():
    '''
    this test is to test the left join function.
    '''
    items_first = Hashtable(1024)
    items_first.add('color', 'blue')
    items_first.add('hello', 'hi')
    
    items_sec = Hashtable(1024)
    items_sec.add('hello', 'greet')
    actual = left_join(items_first,items_sec)
    expected = [['color', 'blue', None], ['hello', 'hi', 'greet']]
    assert actual == expected


def test_left_join_empty_map():
    '''
    this test is to test the left join function if empty map.
    '''
    items_first = Hashtable(1024)
    items_first.add('color', 'blue')
    items_first.add('hello', 'hi')
    
    items_sec = Hashtable(1024)
    actual = left_join(items_first,items_sec)
    expected = [['color', 'blue', None]]
    assert actual == expected


