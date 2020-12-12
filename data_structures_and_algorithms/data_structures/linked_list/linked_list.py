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

    
    def append (self,val):
        '''
        this method will add a new node with the given value to the end of the list
        '''
        node = Node(val)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node


    def includes(self,val):
        current = self.head
        while current != None:
            if current.value == val:
                return True
            current = current.next
            return False


    def insertBefore(self,val,newVal): 
        '''
        this method will add a new node with the given newValue immediately before the first value node
        '''
        node = Node(newVal) # Node(5)
        current = self.head # Node(2)
        # case 1 :  2,3 . insert 5 before 2.
        if current.value == val: # 2 == 2 >> true 
            node.next = current # Node(5).next = Node(2) 
            self.head = node # Node(5) is head >> 5,2,3
        # case 2 :  2,3 . insert 5 before 3.
        else:
            while current.next != None: # Node(3) != none >> true ,, current = Node(2)
                if current.next.value == val: # 3 == 3 >> true
                    node.next = current.next # Node(5).next = Node(3)
                    current.next = node # Node(2).next = Node(5)
                    break # to break while loop
                current = current.next # to move through the list until it met the condition "current.next.value == val"
    
    def insertAfter(self,val, newVal):
        '''
        this method will add a new node with the given newValue immediately after the first value node
        '''
        node = Node(newVal)
        current = self.head
        # case 1 :  2,3 . insert 7 after 2.
        if current.value == val: # Node(2) > 2 == 2 >> true
            n = current.next # n = Node(3)
            current.next = node # Node(2).next = Node(7) >>>> 2,7
            current = current.next # current = Node(7)
            current.next = n # Node(7).next = Node(3)
        # case 2 :  2,3 . insert 7 after 3.
        else:
            while current.next != None:
                if current.next.value == val: # 3 == 3 >> true
                    n = current.next.next # n = None
                    current = current.next # current = Node(3)
                    current.next = node # node(3).next = Node(7) >> node(3) > Node(7)
                    current = current.next # current = Node(7)
                    current.next = n # Node(7).next = none
                    break
                current = current.next # to move through the list until it met the condition "current.next.value == val"


    def kthFromEnd(self,k):
        current = self.head
        new_list = []
        if current == None:
            return 'this is an empty list'
        try:
            while current != None:
                new_list.append(current.value)
                current = current.next
            formatted_list = new_list[::-1]
            return formatted_list[k]
        except IndexError:
            return f'{k} is out of the range'
        except TypeError:
            return 'invalid input'

                 
    def __str__(self):
        current=self.head
        result=''
        if current == None:
            return 'Empty List'
        else:
            while current:
                result += f'{[current.value]}->'
                current=current.next   
            result += f'NULL'
        return result


def zipLists(first_l,sec_l):
    first_l_modified = first_l.split('->')
    sec_l_modified = sec_l.split('->')
    sec_l_modified.pop()
    first_l_modified.pop()
    a=len(first_l_modified)+len(sec_l_modified)
    n=0
    count=1
    t=True
    while True:
        if t:
            first_l_modified.insert(count,sec_l_modified[n])
            count+=1
            n+=1
            t=False
        else:
            first_l_modified.insert(count+n,sec_l_modified[n])
            count+=1
            n+=1

        if len(first_l_modified) == a:
            result=''
            for i in first_l_modified:
                result+=f'{i} -> '
            result+='Null'
            return result


if __name__ == "__main__":

    pass
    a = Linked_list()
    a.append(2)
    a.append(3)
    a.append(4)
    first_list=a.__str__()
    b = Linked_list()
    b.append(5)
    b.append(6)
    b.append(7)
    sec_list=b.__str__()
    print(first_list)
    print(sec_list)

    print(zipLists(first_list,sec_list))
 
