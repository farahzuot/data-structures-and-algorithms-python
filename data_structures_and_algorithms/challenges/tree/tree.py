class Node:
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


class BinarySearchTree(BinaryTree):

    
    def add(self,value):
        self.arr.append(value)
        if self.root == None:
            self.root=Node(value)
        else:
            def internal(node):
                if value < node.value:
                    if node.left == None:
                        node.left = Node(value)
                        return
                    else:
                        internal(node.left)

                else:
                    if node.right == None:
                        node.right = Node(value)
                        return
                    else:
                        internal(node.right)
            internal(self.root)




    def contains(self,value):
        if value in self.arr:
            return True
        else:
            return False



if __name__ == '__main__':
    bt = BinaryTree()
    bt.root = Node(6)
    bt.root.left = Node(5)
    bt.root.right = Node(-1)

    print(bt.preOrder())
    print(bt.inOrder())
    print(bt.postOrder())

