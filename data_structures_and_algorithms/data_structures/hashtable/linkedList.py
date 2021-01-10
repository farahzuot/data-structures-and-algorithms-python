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

                 

