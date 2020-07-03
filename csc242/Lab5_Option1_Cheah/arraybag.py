"""
Ricky Cheah
3/13/20

3/1/20 Added clone method
3/14/20 Added __contains__, increaseSize and decreaseSize
        Modified remove


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
            if not item in other: #uses __contains__ on other
                return False
        return True
    
    def __contains__(self, findItem):
        """
        Returns True if the "findItem" element is found in self._items (only up to len(self) index).
            Also updates self._targetIndex to the found element index.
        Returns False otherwise, and self._targetIndex remains at -1. 
        """
        self._targetIndex = -1
        for i in range(len(self)):
            if self._items[i] == findItem:
                self._targetIndex = i
                return True
        return False
        
    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
        self._size = 0 #will print {None} if don't add this

    def add(self, item):
        """Adds item to self."""
        # Check array memory here and increase it if necessary
        if len(self._items) == len(self): #create larger arrayBag
            self.increaseSize()

        #adding item to arrayBag (or larger arrayBag)
        self._items[len(self)] = item
        self._size += 1
        
    def increaseSize(self):
        """
        Increases the size of the Array by DEFAULT_CAPACITY.
        """
        newArray = Array(len(self._items) + ArrayBag.DEFAULT_CAPACITY)
        for i in range(len(self)):
            newArray[i] = self._items[i]
        self._items = newArray
    
    def decreaseSize(self):
        """
        Decreases the size of the Array by half.
        """
        newArray = Array(len(self._items) // 2)
        for i in range(len(self)):
            newArray[i] = self._items[i]
        self._items = newArray
    

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        # Check precondition and raise if necessary
        try:
            if not item in self:
                raise KeyError(str(item) + " not in bag")
           
            #if KeyError was not raised, execute these code:
            # self._targetIndex created in __contains__
            targetIndex = self._targetIndex

            # Shift items to the left of target up by one position
            for i in range(targetIndex, len(self) - 1):
                self._items[i] = self._items[i + 1]
            self._items[len(self) - 1] = Array.fillValue
            # Decrement logical size
            self._size -= 1
            
            #decrease array size if needed to not waste memory.
            if len(self) <= len(self._items) // 4 and len(self._items) >= self.DEFAULT_CAPACITY*2:
                self.decreaseSize()
            
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


if __name__ == "__main__":
    bag1 = ArrayBag([1,2,3])
    bag2 = ArrayBag([1,2,4])
    print(bag1 == bag2)
    bag1.remove(1)
    print(bag1)

    print(bag1._items)
    bag1.increaseSize()
    print(bag1._items)
    bag1.remove(4)
    bag1.remove(2)
    print(bag1._items)
    bag1.remove(3)
    print(bag1._items)
    print(bag1)
    
