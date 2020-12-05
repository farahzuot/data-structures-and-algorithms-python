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


@pytest.fixture
def a_value():
    a = Linked_list()
    a.insert('Hello')
    a.insert('world')
    return a