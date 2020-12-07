from data_structures_and_algorithms.data_structures.linked_list.linked_list import Linked_list
import pytest


def test_instance():
    ll = Linked_list()
    assert isinstance(ll, Linked_list)

def test_empty_linked_list():
    '''
    this function is to instantiate an empty linked list.
    '''
    acutal = Linked_list()
    assert acutal.head == None

def test_insert(a_value):
    '''
    this function is to insert multiple values into the linked list.
    '''
    assert a_value.__str__() == '{world}->{Hello}->NULL'


def test_includes(a_value):
    '''
    this function Will return false when searching for a value in the linked list that does not exist
    '''
    assert a_value.includes('world')


def test_includes_false(a_value):
    '''
    this function Will return false when searching for a value in the linked list that does not exist
    '''
    assert a_value.includes('farah') == False

def test_append():
    '''
    this function will add a node to the end of the linked list
    '''
    a = Linked_list()
    a.append(2)
    assert a.__str__() == '{2}->NULL'


def test_append_multi(b_value):
    '''
    this function will add multiple nodes to the end of the linked list
    '''
    assert b_value.__str__() == '{2}->{3}->{4}->NULL'

def test_insert_before_middle(b_value):
    '''
    this function will insert a node before a node located i the middle of a linked list
    '''
    b_value.insertBefore(3,5)
    assert b_value.__str__() == '{2}->{5}->{3}->{4}->NULL'

def test_insert_before_first(b_value):
    '''
    this function will insert a node before the first node of a linked list
    '''
    b_value.insertBefore(2,5)
    assert b_value.__str__() == '{5}->{2}->{3}->{4}->NULL'

def test_insert_after_middle(b_value):
    '''
    this function will insert after a node in the middle of the linked list
    '''
    b_value.insertAfter(3,5)
    assert b_value.__str__() == '{2}->{3}->{5}->{4}->NULL'

def test_insert_after_last(b_value):
    '''
    this function will insert a node after the last node of the linked list
    '''
    b_value.insertAfter(4,5)
    assert b_value.__str__() == '{2}->{3}->{4}->{5}->NULL'


def test_kthFromEnd_out_of_range():
    '''
    this case Where k is greater than the length of the linked list
    '''
    index = Linked_list() 
    index.append(1)
    index.append(2)
    assert index.kthFromEnd(3) == '3 is out of the range'

def test_kthFromEnd_k_equal_listLen():
    '''
    this case Where k and the length of the list are the same
    '''
    index = Linked_list() 
    index.append(1)
    index.append(2)
    assert index.kthFromEnd(2) == '2 is out of the range'

def test_kthFromEnd_k_negative():
    '''
    this case Where k is a negative int
    '''
    index = Linked_list() 
    index.append(1)
    index.append(2)
    assert index.kthFromEnd(-1) == 1

def test_kthFromEnd_k_not_int():
    '''
    this case Where k is not an int
    '''
    index = Linked_list() 
    index.append(1)
    index.append(2)
    assert index.kthFromEnd('2') == 'invalid input'

def test_kthFromEnd_list_size_one():
    '''
    this case Where the linked list is of a size 1
    '''
    index = Linked_list() 
    index.append(1)
    assert index.kthFromEnd(0) == 1

def test_kthFromEnd_happy_path():
    '''
    this case where k is not at the end, but somewhere in the middle of the linked list
    '''
    index = Linked_list() 
    index.append(1)
    index.append(2)
    index.append(3)
    assert index.kthFromEnd(1) == 2

@pytest.fixture
def a_value():
    a = Linked_list()
    a.insert('Hello')
    a.insert('world')
    return a

@pytest.fixture
def b_value():
    b = Linked_list()
    b.append(2)
    b.append(3)
    b.append(4)
    return b