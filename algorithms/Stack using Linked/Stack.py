from Intnode import *

class EmptyContainerError(Exception):
    pass

class Stack():

    def __init__(self):
        self._contents = None

    def enqueue(self, item):
        new_node = Intnode(item)
        new_node.next = self._contents
        self._contents = new_node

    def dequeue(self):
        if(self.is_empty()):
            raise EmptyContainerError
        else:
            item = self._contents._value
            self._contents = self._contents.next
        return item

    def is_empty(self):
        return not(self._contents)
