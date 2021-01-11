# from tree import BinaryTree,NodeTwo

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

def tree_intersection(tree_one,tree_two):
    first = tree_one.preOrder()
    second = tree_two.preOrder()
    common = []
    for i in first:
        if i in second:
            common.append(i)

    return common



if __name__ == "__main__":
    bt = BinaryTree()
    bt.root = NodeTwo(6)
    bt.root.left = NodeTwo(5)
    bt.root.right = NodeTwo(-1)

    bt_two = BinaryTree()
    bt_two.root = NodeTwo(6)
    bt_two.root.left = NodeTwo(0)
    bt_two.root.right = NodeTwo(-1)

    print(tree_intersection(bt, bt_two))