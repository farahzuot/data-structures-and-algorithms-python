from data_structures_and_algorithms.challenges.tree.tree import BinarySearchTree, BinaryTree, NodeTwo

def test_empty_tree():
    '''
    Can successfully instantiate an empty tree
    '''
    bt = BinaryTree()
    assert bt.preOrder() == []

def test_single_tree():
    '''
    Can successfully instantiate a tree with a single root node
    '''
    bt = BinaryTree()
    bt.root = NodeTwo(2)
    assert bt.preOrder() == [2]

def test_single_tree_left_right():
    '''
    Can successfully add a left child and right child to a single root node
    '''
    bt = BinaryTree()
    bt.root = NodeTwo(2)
    bt.root.left=NodeTwo(3)
    bt.root.right=NodeTwo(4)
    assert bt.preOrder() == [2,3,4]

def test_single_tree_preorder():
    '''
    Can successfully return a collection from a preorder traversal
    '''
    bt = BinaryTree()
    bt.root = NodeTwo(2)
    bt.root.left=NodeTwo(3)
    bt.root.right=NodeTwo(4)
    assert bt.preOrder() == [2,3,4]

def test_single_tree_inorder():
    '''
    Can successfully return a collection from an inorder traversal
    '''
    bt = BinaryTree()
    bt.root = NodeTwo(2)
    bt.root.left=NodeTwo(3)
    bt.root.right=NodeTwo(4)
    assert bt.inOrder() == [3,2,4]

def test_single_tree_postorder():
    '''
    Can successfully return a collection from a postorder traversal
    '''
    bt = BinaryTree()
    bt.root = NodeTwo(2)
    bt.root.left=NodeTwo(3)
    bt.root.right=NodeTwo(4)
    assert bt.postOrder() == [3,4,2]


def test_max_binary_tree():
    bt = BinaryTree()
    bt.root = NodeTwo(6)
    bt.root.left = NodeTwo(5)
    bt.root.right = NodeTwo(-1)
    bt.root.right.left = NodeTwo(8)
    bt.root.right.right = NodeTwo(14)
  
    assert bt.find_maximum_value() == 14

def test_breadth_first():
    bt = BinaryTree()
    bt.root = NodeTwo(6)
    bt.root.left = NodeTwo(5)
    bt.root.right = NodeTwo(-1)
    bt.root.right.left = NodeTwo(8)
    bt.root.right.right = NodeTwo(14)
  
    assert bt.breadthFirst() == [6, 5, -1, 8, 14]


def test_breadth_first_empty():
    bt = BinaryTree()
    assert bt.breadthFirst() == 'Empty tree'


