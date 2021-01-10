# from linkedList import Linked_list
class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None

class Linked_list:
    def __init__(self):
        self.head = None

    def insert(self,key,val):
        node = Node(key,val)
        if self.head == None:
            self.head = node
        else:
            node.next=self.head
            self.head=node

                 
class Hashtable:
    def __init__(self, size):
        self.size = size
        self.map = [None]*size
        # self.ll = Linked_list()

    def hash(self, key):
        ascii = 0
        for i in key:
            ascii += ord(i)
        hashed = ascii * 17
        hashed = hashed % self.size
        return hashed

    def add(self, key, value):
        index = self.hash(key)
        if not self.map[index]:
            self.map[index] = Linked_list()
            self.map[index].insert(key,value)    
        else:
            self.map[index].insert(key,value) 


    def get(self, key):
        index = self.hash(key)
        if not self.map[index]:
            return self.map[index]
        else:
            current = self.map[index].head
            while current:
                if current.key == key:
                    return current.value
                current = current.next


    def contains(self, key):
        index = self.hash(key)
        if not self.map[index]:
            return False
        return True





if __name__=='__main__':
    items = Hashtable(1024)
    items.add('roloc', 'red')
    items.add('color', 'blue')
    items.add('coolr', 'cold')
    items.add('hello', 'hi')
    print(items.hash('hello'))
    # print(items.map[items.hash('color')])
    # print(items.contains('co;;lro'))
    print(items.get('rol;;oc'))
    # print(items.map)