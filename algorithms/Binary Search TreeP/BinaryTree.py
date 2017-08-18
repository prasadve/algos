class BTNode:
    '''A class that represents a BTNode'''
    def __init__(self, data, left = None, right = None):
        '''(BTNode) -> NoneType
        A method that initializes a BTNode object
        '''
        self._data = data
        self._left = left
        self._right = right

class BinarySearchTree:
    '''A class that represents a BinaryTree'''
    def __init__(self):
        '''(BinaryTree) -> NoneType
        A method that initializes a BinaryTree
        '''
        self._root = None

    def insert(self, value):
        '''(BinarySearchTree) -> NoneType
        This method inserts a new node with .data = value
        '''
        new_node = BTNode(value)
        if(self._root == None):
            self._root = new_node
        else:
            curr = self._root
            parent = None
            while((curr is not None)):
                parent = curr
                if(value < curr._data):
                    curr = curr._left
                else:
                    curr = curr._right
            if(parent._data > value):
                parent._left = new_node
            else:
                parent._right = new_node

    def search(self, value):
        '''(BinarySearchTree) -> Bool
        This method returns true iff the BST contains
        a node with the data = value
        '''
        result = False
        if(self._root is not None):
            curr = self._root
            while((curr is not None) and (result is not True)):
                if(curr._data == value):
                    result = True
                elif(value < curr._data):
                    curr = curr._left
                else:
                    curr = curr._right
        return result

    def find_smallest(self):
        '''(BinarySearchTree) -> int
        This method return the data of the smallest.
        Returns None if the BST is empty == None
        '''
        result = None
        if(self._root is not None):
            curr = self._root
            while curr._left is not None:
                curr = curr._left
            result = curr._data
        return result

    def find(self, value):
        '''(BinarySearchTree) -> (object, object)
        This method returns the node with the data= value
        and its parent. If it doesnt exist then (None, None)
        is returned
        '''
        curr = self._root
        parent = None
        while((curr is not None) and (curr._data != value)):
            parent = curr
            if(value < curr._data):
                curr = curr._left
            else:
                curr = curr._right
        if(curr == None):
            result = (None, None)
        else:
            result = (curr, parent)
        return result

    def find_smallest_and_parent(self):
        '''(find_smallest_and_parent) -> (object, object)
        This method return the node of the smallest and its parent.
        If the tree is empty then the (None, None) is returned and
        If the smallest is the root then the parent is None.
        '''
        curr = self._root
        parent = None
        while((curr._left is not None)):
            parent = curr
            curr = curr._left
        return (curr, parent)
