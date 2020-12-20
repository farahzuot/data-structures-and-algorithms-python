from data_structures_and_algorithms.challenges.tree.tree import BinarySearchTree, BinaryTree, Node

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
    bt.root = Node(2)
    assert bt.preOrder() == [2]

def test_single_tree_left_right():
    '''
    Can successfully add a left child and right child to a single root node
    '''
    bt = BinaryTree()
    bt.root = Node(2)
    bt.root.left=Node(3)
    bt.root.right=Node(4)
    assert bt.preOrder() == [2,3,4]

def test_single_tree_preorder():
    '''
    Can successfully return a collection from a preorder traversal
    '''
    bt = BinaryTree()
    bt.root = Node(2)
    bt.root.left=Node(3)
    bt.root.right=Node(4)
    assert bt.preOrder() == [2,3,4]

def test_single_tree_inorder():
    '''
    Can successfully return a collection from an inorder traversal
    '''
    bt = BinaryTree()
    bt.root = Node(2)
    bt.root.left=Node(3)
    bt.root.right=Node(4)
    assert bt.inOrder() == [3,2,4]

def test_single_tree_postorder():
    '''
    Can successfully return a collection from a postorder traversal
    '''
    bt = BinaryTree()
    bt.root = Node(2)
    bt.root.left=Node(3)
    bt.root.right=Node(4)
    assert bt.postOrder() == [3,4,2]


def test_max_binary_tree():
    bt = BinaryTree()
    bt.root = Node(6)
    bt.root.left = Node(5)
    bt.root.right = Node(-1)
    bt.root.right.left = Node(8)
    bt.root.right.right = Node(14)
  
    assert bt.find_maximum_value() == 14

