from data_structures_and_algorithms.challenges.tree_intersection.tree_intersection import tree_intersection,BinaryTree,NodeTwo


def test_tree_intersection_happy_path():
    '''
    Can successfully return a set of values found in both trees
    '''
    bt = BinaryTree()
    bt.root = NodeTwo(6)
    bt.root.left = NodeTwo(5)
    bt.root.right = NodeTwo(-1)

    bt_two = BinaryTree()
    bt_two.root = NodeTwo(6)
    bt_two.root.left = NodeTwo(0)
    bt_two.root.right = NodeTwo(-1)

    actual = tree_intersection(bt, bt_two)
    expected = [6, -1]
    assert actual == expected


def test_tree_intersection_Empty_tree():
    '''
    Can successfully return empty list when one of the trees is empty
    '''
    bt = BinaryTree()
    bt.root = NodeTwo(6)
    bt.root.left = NodeTwo(5)
    bt.root.right = NodeTwo(-1)

    bt_two = BinaryTree()
    actual = tree_intersection(bt, bt_two)
    expected = []
    assert actual == expected


def test_tree_intersection_Empty_both_trees():
    '''
    Can successfully return empty list when both of the trees are empty
    '''
    bt = BinaryTree()
    bt_two = BinaryTree()
    actual = tree_intersection(bt, bt_two)
    expected = []
    assert actual == expected
