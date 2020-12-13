from data_structures_and_algorithms.data_structures.queue_with_stacks.queue_with_stacks import PseudoQueue,Stack

def test_enqueue():
    '''
    function will test if the parameter is added or not.
    '''
    q = PseudoQueue()
    assert q.enqueue(7) == '7 -> 2 -> 1 -> None'



def test_enqueue_invalid_input():
    '''
    function will test if the input is valid
    '''
    q = PseudoQueue()
    assert q.enqueue('hi') == 'invalid input'




def test_dequeue():
    '''
    function will test if poped item is the first in to be like first in first out.
    '''
    q = PseudoQueue()
    q.enqueue(7)
    assert q.dequeue() == 1
