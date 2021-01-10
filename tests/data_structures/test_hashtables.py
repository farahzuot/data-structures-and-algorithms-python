from data_structures_and_algorithms.data_structures.hashtable.hashtable import Hashtable



def test_null_key_not_exist():
    '''
    returns null for a key that does not exist in the hashtable
    '''
    items = Hashtable(1024)
    actual = items.get('rol;;oc')
    expected = None
    assert actual == expected

def test_Adding_key_value():
    '''
    Adding a key/value to your hashtable results in the value being in the data structure
    '''
    items = Hashtable(1024)
    items.add('color', 'blue')
    actual = items.get('color')
    expected = 'blue'
    assert actual == expected

def test_Retrieving_based_on_key():
    '''
    this function is to Retrieving based on a key returns the value stored
    '''
    items = Hashtable(1024)
    items.add('hello', 'hi')
    actual = items.get('hello')
    expected = 'hi'
    assert actual == expected

def test_handle_collision():
    '''
    this function is to retrieve a value from a bucket within the hashtable that has a collision and handle a collision within the hashtable
    '''
    items = Hashtable(1024)
    items.add('hello', 'hi')
    items.add('helol', '42')
    actual = items.get('helol')
    expected = '42'
    assert actual == expected

def test_hash_key():
    '''
    this function is to hash a key to an in-range value
    '''
    items = Hashtable(1024)
    actual = items.hash('hello')
    expected = 852
    assert actual == expected
