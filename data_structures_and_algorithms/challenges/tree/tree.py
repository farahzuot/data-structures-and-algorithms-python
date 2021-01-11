class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

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
        

class NodeTwo:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class BinaryTree():
    def __init__(self):
        self.root=None
        self.arr=[]

    def preOrder(self):
        try:
            result = []
            def internal(node):
                result.append(node.value)
                if node.left:
                    internal(node.left)
                if node.right:
                    internal(node.right)
            internal(self.root)
            return result
        except AttributeError:
            return []

    def inOrder(self):
        try:
            result=[]
            def internal(node):
                if node.left:
                    internal(node.left)
                result.append(node.value)
                if node.right:
                    internal(node.right)
            internal(self.root)
            return result
        except AttributeError:
            return []

    def postOrder(self):
        try:
            result=[]
            def internal(node):
                if node.left:
                    internal(node.left)
                if node.right:
                    internal(node.right)
                result.append(node.value)

            internal(self.root)
            return result
        except AttributeError:
            return []
   
    def find_maximum_value(self):
        try:
            result = []
            result.append(0)
            def internal(node):
                if node.value > result[0]:
                    result[0] = node.value
                if node.left:
                    internal(node.left)
                if node.right:
                    internal(node.right)
            internal(self.root)
            return result[0]
        except AttributeError:
            return []

    def breadthFirst(self,result =[]): 
        try: 
            queue = Queue()
            queue.enqueue(self.root)    
            while queue.front:
                curr = queue.front
                if curr.value.left:
                    queue.enqueue(curr.value.left)
                if curr.value.right:
                    queue.enqueue(curr.value.right)
                result.append(curr.value.value)
                queue.dequeue()
            return result
        except AttributeError:
            return 'Empty tree'




class BinarySearchTree(BinaryTree):
    def add(self,value):
        self.arr.append(value)
        if self.root == None:
            self.root=NodeTwo(value)
        else:
            def internal(node):
                if value < node.value:
                    if node.left == None:
                        node.left = NodeTwo(value)
                        return
                    else:
                        internal(node.left)

                else:
                    if node.right == None:
                        node.right = NodeTwo(value)
                        return
                    else:
                        internal(node.right)
            internal(self.root)




    def contains(self,value):
        if value in self.arr:
            return True
        else:
            return False

