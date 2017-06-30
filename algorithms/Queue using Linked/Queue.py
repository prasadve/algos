from Intnode import *

class EmptyContainerError(Exception):
    pass

class Queue():

    def __init__(self):
        # Creating linked list with None
        self._contents = None

    def enqueue(self, item):
        new_node = Intnode(item)
        new_node.next = self._contents
        self._contents  = new_node

    def dequeue(self):
        if(self.is_empty()):
            raise EmptyContainerError
        else:
            if(self._contents.next == None):
                item = self._contents._value
                self._contents = self._contents._next
            else:
                curr = self._contents
                prev = None
                while curr.next != None:
                    prev = curr
                    curr = curr.next
                item = curr._value
                prev.next = curr.next
        return item

    def is_empty(self):
        return not(self._contents)
