# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.next=None

# class Linked_list:
#     def __init__(self):
#         self.head = None
#         self.arr =[]

#     def insert(self,val):
#         node = Node(val)
#         if self.head == None:
#             self.head = node
#             current = self.head
#         else:
#             current = self.head
#             while current.next != None:
#                 current = current.next
#             current.next = node
#         self.arr.append(current)

#     def includes(self,val2):
#         current = self.head
#         while current != None:
#             if current.value == val2:
#                 return True
#             current = current.next
#             return False
   

#     def __str__(self):
#         return f" { self.arr } "


# if __name__ == "__main__":
#     data = Node(3)
#     data2 = Node(4)
#     data2.next = data
#     c = Linked_list()
