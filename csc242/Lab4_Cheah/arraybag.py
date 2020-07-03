"""
Ricky Cheah
3/1/20
Added clone method 

File: arraybag.py
Original Author: Ken Lambert

"""

from arrays import Array

class ArrayBag(object):
    """An array-based bag implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self) == 0
    
    def __len__(self):
        """Returns the number of items in self."""
        return self._size

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = ArrayBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False
        for item in self:
            if not item in other:
                return False
        return True

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        # Exercise
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
        self._size = 0 #will print {None} if don't add this

    def add(self, item):
        """Adds item to self."""
        # Check array memory here and increase it if necessary
        if len(self._items) == len(self): #create larger arrayBag
            newList = Array(len(self._items) + ArrayBag.DEFAULT_CAPACITY)
            #copy items to new arrayBag
            #can't use add because this is add's code, use indexing instead. 
            #this can be avoided by creating a new bag enlarging method,
            #   separate from this add method
            for i in range(len(self)):
                newList[i] = self._items[i]
            self._items = newList
        
        #adding item to arrayBag (or larger arrayBag)
        self._items[len(self)] = item
        self._size += 1
        

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        # Check precondition and raise if necessary
        try:
            if not item in self:
                raise KeyError(str(item) + " not in bag")
            # Search for the index of the target item
            targetIndex = 0
            for targetItem in self:
                if targetItem == item:
                    break
                targetIndex += 1
            # Shift items to the left of target up by one position
            for i in range(targetIndex, len(self) - 1):
                self._items[i] = self._items[i + 1]
            # Decrement logical size
            self._size -= 1
            # Check array memory here and decrease it if necessary
            # Exercise
        except KeyError:
            print(str(item) + " not in bag.")
    
    def clone(self):
        """
        When called on an existing ArrayBag object, returns an exact ArrayBag 
        copy.
        """
        newBag = ArrayBag()
        for i in range(len(self)):
            newBag.add(self._items[i])
        return newBag
        
        
