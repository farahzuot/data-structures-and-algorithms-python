class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Linked_list:
    def __init__(self):
        self.head = None

    def insert(self,val):
        node = Node(val)
        if self.head == None:
            self.head = node
        else:
            node.next=self.head
            self.head=node

    def includes(self,val2):
        current = self.head
        while current != None:
            if current.value == val2:
                return True
            current = current.next
            return False
   

    def __str__(self):
        current=self.head
        result=''
        if current == None:
            return 'Empty List'
        else:
            while current:
                result += f'{{{current.value}}}->'
                current=current.next   
            result += f'NULL'
        return result


if __name__ == "__main__":
    pass
    # data = Node(3)
    # data2 = Node(4)
    # data2.next = data
    # c = Linked_list()
