# not generic.. the values should then have a compare method
class BSTBSTNode:
    left = None
    right = None
    value = None

    def __init__(value):
        self.value = value
    def addChild (value):
        if (value > self.value):# and self.right == None):
            if (self.right == None):
                self.right = BSTNode(value)
            else:
                self.right.addChild(value)
        else: # (value <= self.value and self.right == None):
            if (self.left == None):
                self.left = BSTNode(value)
            else:
                self.left.addChild(value)


class BinarySearchTree:
    root = None
    def __init__(root_value):
        self.root = BSTNode(root_value)

    def insert (value):
        self.root.addChild(value)



BST = BinarySearchTree(5)

BST.insert(2)
BST.insert(6)
BST.insert(10)
