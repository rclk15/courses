"""
Ricky Cheah
4/1/2020

Module for LinkedListIterator Class. 
Can be used to iterate over and mutate LinkedList objects.
"""
from node import TwoWayNode #TwoWayNode(data, previous, next)

class LinkedListIterator(object):
    """Represents the list iterator for a linked list."""
    
    def __init__(self, backingStore):
        self._backingStore = backingStore
        self._modCount = backingStore.getModCount()
        self.first()

    def first(self):
        """Returns the cursor to the beginning of the backing store."""
        self._cursor = self._backingStore._head #points to the head sentinel. 
        self._cursorPosition = 0 #for use by hasNext and hasPrevious
        self._lastMovement = None
        
    def hasNext(self):
        """Returns True if the iterator has a next item or False otherwise."""
        return self._cursorPosition < len(self._backingStore)
    
    def next(self):
        """Preconditions: hasNext returns True
        The list has not been modified except by this iterator's mutators.
        Returns the current item and advances the cursor to the next item.
        Postcondition: lastMovement is now defined."""
        if not self.hasNext():
            raise ValueError("No next item in list iterator")
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("Illegal modification of backing store")

        self._lastMovement = "Next"
        self._cursor = self._cursor.next
        self._cursorPosition += 1
        return self._cursor.data
    
    def last(self):
        """Moves the cursor to the end of the backing store."""
        self._cursor = self._backingStore._head
        self._cursorPosition = len(self._backingStore)
        self._lastMovement = None
        
    def hasPrevious(self):
        """Returns True if the iterator has a previous item or False otherwise."""
        return self._cursorPosition > 0
    
    def previous(self):
        """Preconditions: hasPrevious returns True
        The list has not been modified except by this iterator's mutators.
        Returns the current item and moves the cursor to the previous item.
        Postcondition: lastMovement is now defined."""
        if not self.hasPrevious():
            raise ValueError("No previous item in list iterator")
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("Illegal modification of backing store")
    
        self._lastMovement = "Prev"
        self._cursor = self._cursor.previous
        self._cursorPosition -= 1
        return self._cursor.data
    


    def insert(self, item):
        """
        Preconditions: the current position is defined
        The list has not been modified except by this iterator's mutators.
        
        Inserts the item at current cursor position."""
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("List has been modified illegally.")
        if self._lastMovement == None: #insert to last position
            theNode = self._backingStore._head
        else:
            theNode = self._cursor 
        
        # this portion ensures a constant time operation b/c 
        # the cursor is already where we want it. 
        newNode = TwoWayNode(item, theNode.previous, theNode)
        theNode.previous.next = newNode
        theNode.previous = newNode
        self._backingStore._size += 1
        self._backingStore.incModCount()
        self._modCount += 1
        self._lastMovement = None

    def remove(self):         
        """Preconditions: the current position is defined (if we successfully moved cursor previously)
        The list has not been modified except by this iterator's mutators.
        
        Pops the item at the current position."""
        if self._lastMovement == None:
            raise AttributeError("The current position is undefined.")
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("List has been modified illegally.")

        # this portion ensures a constant time operation b/c 
        # the cursor is already where we want it. 
        theNode = self._cursor
        item = theNode.data
        theNode.previous.next = theNode.next
        theNode.next.previous = theNode.previous
        self._backingStore._size -= 1
        self._backingStore._modCount -= 1
        
        #need to move cursor back one step if previous command was "next"
        #to keep cursor at the same position. 
        if self._lastMovement == "Next":
            self._cursorPosition -= 1
        self._modCount -= 1
        self._lastMovement = None
        
    def replace(self, item):
        """Preconditions: the current position is defined (if we successfully moved cursor previously)
        The list has not been modified except by this iterator's mutators.
        
        Replaces the list element at the current position with "item" parameter.
        """
        if self._lastMovement == None:
            raise AttributeError("The current position is undefined.")
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("List has been modified illegally.")
        
        self._cursor.data = item
        self._lastMovement = None
        


        