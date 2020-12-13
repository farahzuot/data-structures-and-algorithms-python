# from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import Stack

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self): 
        self.top = None
    

    def push(self,data):
        node = Node(data)
        if self.top == None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def peek(self):
        try:
            return self.top.value
        except AttributeError:
            return 'Empty Stack!'

    def pop(self):
        try:
            self.top = self.top.next
        except AttributeError:
            return 'Empty Stack!'

    
    def isEmpty(self):
        if self.top:
            return False
        else:
            return True
  

    def __str__(self):
        result = ''
        current = self.top
        if not current:
            result = 'Empty stack!'
        else:
            while current:
                result += f'{current.value} -> ' 
                current = current.next
            result+= 'None'
        return result

class PseudoQueue:

    def __init__(self):
        # 3 -> 2 -> 1 -> None filo
        self.first_stack = Stack()
        self.sec_stack = Stack()
        self.first_stack.push(1)
        self.first_stack.push(2)


    def enqueue(self,value): # fifo 1 -> 2 -> 3 -> None
        '''
        this function is to inserts value into the PseudoQueue, using a first-in, first-out approach.
        '''
        if type(value) != int:
            return 'invalid input'
        self.first_stack.push(value)
        return(self.first_stack.__str__())

        
    def dequeue(self):
        '''
        this function is to extracts a value from the PseudoQueue, using a first-in, first-out approach.
        '''
        while True:
            if self.first_stack.isEmpty() != True:
                top = self.first_stack.peek()
                self.first_stack.pop()
                self.sec_stack.push(top)
            else:
                break 
        sec_top = self.sec_stack.peek()     
        self.sec_stack.pop()
        while True:
            if self.sec_stack.isEmpty() != True:
                top_two = self.sec_stack.peek()
                self.sec_stack.pop()
                self.first_stack.push(top_two)
            else:
                break 
        return sec_top


if __name__ == "__main__":
    pass
    # a = PseudoQueue()
    # print(a.enqueue(7))
    # print(a.dequeue())
