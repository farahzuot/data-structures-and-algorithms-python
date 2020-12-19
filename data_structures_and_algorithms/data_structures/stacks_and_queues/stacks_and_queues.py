class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self): # Node1 - > Node 2
        self.top = None
        self.arr = []
    

    def push(self,data):
        node = Node(data)
        self.arr.append(node.value)
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
    
    def max(self):
        print(self.arr)
        max = 0
        for i in self.arr:
            if i > max:
                max=i
        print(max)
        return max


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
        

if __name__ == "__main__":
    pass
    a = Stack()
    # b = Queue()
    # print(b.isEmpty())
    # b.enqueue(1)
    # b.enqueue(4)
    # print(b.peek())
    # b.enqueue(6)
    # b.dequeue()
    # b.enqueue(9)
    # b.dequeue()
    # b.dequeue()
    # print(b.__str__())
    a.push(1)
    a.push(2)
    a.push(8)
    a.push(3)
    # print(a.isEmpty())
    # a.pop()
    # print(a.peek())
    a.max()

  




