class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,data): # 1 -> 2 -> none
        node = Node(data)
        if self.front == None:
            self.front = node # 1 - >
        else:
            self.rear = self.front 
            current = self.rear # curr = node(1)
            while current:
                if current.next == None:
                    current.next = node
                    break               
                current = current.next

    def dequeue(self):
        try:
            self.front = self.front.next
        except AttributeError:
            return ('Empty stack!')
    
    def peek(self):
        try:
            return self.front.value
        except AttributeError:
            return ('Empty stack!')
    
    def isEmpty(self):
        if self.front:
            return False
        else:
            return True

    def __str__(self):
        result=''
        current = self.front
        if current == None:
            result = 'Empty stack!'
        else:
            while current:
                result += f'{current.value} -> '
                current = current.next
            result += 'None'
        return result