# from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import Queue
# from collections import deque
from queue import Queue

class AnimalShelter(Queue):
    def __init__(self):
        self.dog_queue = Queue()
        self.cat_queue = Queue()
    
    def enqueue(self,animal):
        pass
    
    def dequeue(self,pref):
        pass

class Cat:
    def __init__(self,name):
        self.name = name
        self.kind = 'cat'

class Dog:
    def __init__(self,name):
        self.name = name
        self.kind = 'dog'

if __name__ == "__main__":
    a = AnimalShelter()
    a.enqueue('Dog')