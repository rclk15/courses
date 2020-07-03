"""
Ricky Cheah
2/24/2020

File: arrays.py

An Array is a restricted list whose clients can use
only [], len, iter, and str.

To instantiate, use

<variable> = array(<capacity>, <optional fill value>)

The fill value is None by default.

Original Code by Ken Lambert
removeItem error portion and RemoveError class by Ivan Temesvari.  
"""
class RemoveError(RuntimeError):
    def __init__(self, arg):
        self.arg = arg
    def __str__(self):
        return(repr(self.value))

class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed at each position. Sets logical size to 0"""
        self._logicalSize = 0
        self._items = list()
        for count in range(capacity):
            self._items.append(fillValue)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self._items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self._items)

    def __iter__(self):
        """Supports iteration over a view of an array."""
        return iter(self._items)

    def __getitem__(self, index):
        """Subscript operator for access at index."""
        return self._items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""
        self._items[index] = newItem
        self._logicalSize += 1
    
    def logicalSize(self):
        """returns current logical size of array."""
        return self._logicalSize
            
    def doubleArraySize(self):
        """method to double array size and copy existing elements into new array"""
        newList = list()
        for i in range(len(self._items)):
            newList.append(self._items[i])
        for count in range(len(self._items)):
            newList.append(None)
        self._items = newList  
        
    def insertItem(self, position, item):
        """
        Method to insert item at specific position(index).
        """
        #position is larger than array size, keep doubling array until we can fit new item. 
        if position > len(self._items)-1:
            while position > len(self._items)-1: #might have to double size more than once
                self.doubleArraySize()
            self._items[position] = item
        #the last position is not empty, meaning we can't shift current elements up.
        #double array size and shift everything up before inserting item.
        elif self._items[len(self._items)-1] != None:
            self.doubleArraySize()
            for i in range(len(self._items)-1, position, -1):
                self._items[i] = self._items[i-1]
            self._items[position] = item
        #simply shift every element up and insert array at position. 
        else:
            for i in range(len(self._items)-1, position, -1):
                self._items[i] = self._items[i-1]
            self._items[position] = item
        self._logicalSize += 1 #add logical size after adding element
    
    def removeItem(self,position):
        """
        Method to remove item at specific position(index).
        """
        try: #raises error if position is out of range or if position contains nothing.
            if(position < 0 or position >= len(self._items)):
                raise RemoveError("Bad index.")
                return False
            elif not self._items[position]:
                raise RemoveError("Position is empty. Returning None")
                return False
        except RemoveError as err:
            print(err.arg)
        else: #shift all elements down to occupy space of removed item, and set last vacated cell to None.
            returnValue = self._items[position]
            for i in range(position,len(self._items)-1):
                self._items[i] = self._items[i+1]
            self._items[len(self._items)-1] = None #set vacated cell back to None
            self._logicalSize -= 1 #decrease logical size after removing element
            return returnValue
            
        
    def __eq__(self, comparedArray):
        """
        allows the use of == to compare arrays.
        Only returns true if the arrays are identical (same size and element positions)
        """
        if type(self) != type(comparedArray):
            raise TypeError("This is not an array!")
            return False
        else:
            if len(self._items) != len(comparedArray):
                print("Arrays are not of same length!")
                return False
            else:
                for i in range(len(self._items)):
                    if self._items[i] != comparedArray[i]:
                        print("The arrays are not equal to each other.")
                        return False
        print("The arrays are equal to each other.")
        return True
