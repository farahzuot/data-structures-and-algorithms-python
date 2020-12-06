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