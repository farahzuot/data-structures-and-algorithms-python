from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import Stack,Queue,Node
import pytest

def test_push_to_stack(a_val):
    '''
    push onto a stack
    '''
    assert a_val.__str__() == '2 -> None'

def test_push_to_stack_mutiple_values(a_val):
    '''
    push multiple values onto a stack
    '''
    a_val.push(3)
    assert a_val.__str__() == '3 -> 2 -> None'

def test_pop_off_stack(a_val):
    '''
    pop off the stack
    '''
    a_val.push(3)
    a_val.pop()
    assert a_val.__str__() == '2 -> None'

def test_pop_until_empty_stack(a_val):
    '''
    empty a stack after multiple pops
    '''
    a_val.push(3)
    a_val.pop()
    a_val.pop()
    assert a_val.__str__() == 'Empty stack!'

def test_peek_top_value(a_val):
    '''
    peek the next item on the stack
    '''
    a_val.push(3)
    a_val.peek()

    assert a_val.peek() == 3

def test_peek_raise_exception():
    '''
    peek on empty stack raises exception
    '''
    a = Stack()
    a.peek()
    assert a.peek() == 'Empty Stack!'


def test_instantiate_empty_stack():
    '''
    instantiate an empty stack
    '''
    a = Stack()
    assert a.__str__() == 'Empty stack!'

@pytest.fixture
def a_val():
    a = Stack()
    a.push(2)
    return a

@pytest.fixture
def b_val():
    b = Queue()
    b.enqueue(2)
    return b

def test_enqueue_to_stack(b_val):
    '''
    enqueue into a queue
    '''
    assert b_val.__str__() == '2 -> None'

def test_enqueue_multible_values_to_stack(b_val):
    '''
    enqueue multiple values into a queue
    '''
    b_val.enqueue(3)
    assert b_val.__str__() == '2 -> 3 -> None'

def test_dequeue_value_from_stack(b_val):
    '''
    dequeue out of a queue the expected value
    '''
    b_val.enqueue(3)
    b_val.dequeue()
    assert b_val.__str__() == '3 -> None'

def test_peek_value(b_val):
    '''
    peek into a queue, seeing the expected value
    '''
    b_val.enqueue(3)
    assert b_val.peek() == 2

def test_dequeue_empty_the_stack(b_val):
    '''
    empty a queue after multiple dequeues
    '''
    b_val.enqueue(3)
    b_val.dequeue()
    b_val.dequeue()
    assert b_val.__str__() == 'Empty stack!'

def test_instantiate_empty_queue():
    '''
    instantiate an empty queue
    '''
    b = Queue()
    assert b.__str__() == 'Empty stack!'

def test_raises_exception():
    '''
    peek on empty queue raises exception
    '''
    b = Queue()
    assert b.peek() == 'Empty stack!'
