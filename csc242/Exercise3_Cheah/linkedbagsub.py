"""
Ricky Cheah
3/5/20
Added clone method 3/1
Became subclass of AbstractBag 3/5

File: linkedbag.py
Original Author: Ken Lambert
"""

"""   
Methods moved to abstractbag.py:
    clone, isEmpty, __len__, __str__, __eq__, __add__
"""


from node import Node
from abstractbag import AbstractBag

class LinkedBagSub(AbstractBag):
    """A link-based bag implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present.
        **Items will be in reverse order of sourceCollection!
        """
        if AbstractBag.TRACE:
            print("linkedbag's __init__")
        self._items = None
        AbstractBag.__init__(self, sourceCollection) #calls init of parent class


    def __iter__(self):
        """Supports iteration over a view of self."""
        if AbstractBag.TRACE:
            print("linkedbag's iter")
            
        cursor = self._items
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        if AbstractBag.TRACE:
            print("linkedbag's clear")
            
        self._items = None
        self._size = 0

    def add(self, item):
        """Adds item to self.
        At the front of the list!
        """
        
        if AbstractBag.TRACE:
            print("linkedbag's add")
            
        self._items = Node(item, self._items)
        self._size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        
        if AbstractBag.TRACE:
            print("linkedbag's remove")
            
        # Check precondition and raise if necessary
        try:
            if not item in self:
                raise KeyError(str(item) + " not in bag")
            # Search for the node containing the target item
            # probe will point to the target node, and trailer
            # will point to the one before it, if it exists
            probe = self._items
            trailer = None
            for targetItem in self:
                if targetItem == item:
                    break
                trailer = probe
                probe = probe.next
            # Unhook the node to be deleted, either the first one or one
            # thereafter
            if probe == self._items:
                self._items = self._items.next
            else:
                trailer.next = probe.next
            # Decrement logical size
            self._size -= 1
        except KeyError:
            print(str(item) + " not in bag.")


if __name__ == '__main__':
    
    bag1 = LinkedBagSub([1,2,3])
    print(bag1)
    bag2 = bag1.clone()
    print(bag2)
    
    for item in bag1:
        print(item)