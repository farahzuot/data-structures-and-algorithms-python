
from data_structures_and_algorithms.data_structures.linked_list.linked_list import Linked_list

def test_instance():
    ll = Linked_list()
    assert isinstance(ll, Linked_list)

def test_empty_linked_list():
    acutal = Linked_list()
    assert acutal.head == None

def test_insert():
    a = Linked_list()
    a.insert('Hello')
    a.insert('world')
    b = a.includes('world')
    assert a.__str__() == '{world}->{Hello}->NULL'


def test_includes():
    a = Linked_list()
    a.insert('Hello')
    a.insert('world')
    assert a.includes('world')
