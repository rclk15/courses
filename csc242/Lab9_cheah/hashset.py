"""
Ricky Cheah
4/17/2020

Added cellLoadFactor, printChains

File: hashset.py
An hash-based set.
Original Author: Ken Lambert
"""

from node import Node
from arrays import Array
from abstractcollection import AbstractCollection
from abstractset import AbstractSet

class HashSet(AbstractCollection, AbstractSet):
    """Represents a hash-based set."""

#    DEFAULT_CAPACITY = 8

    def __init__(self, sourceCollection = None, inputCapacity = 8):
        self._array = Array(inputCapacity)
        self._foundNode = self._priorNode = None
        self._index = -1
        #this has to be before the AbstractCol.__init__ b/c init will use self._loadedCells
        self._loadedCells = 0 
        AbstractCollection.__init__(self, sourceCollection) 


    # Accessor methods
    def __contains__(self, item):
        """Returns True if item is in self or False otherwise."""
        self._index = abs(hash(item)) % len(self._array)
        self._priorNode = None
        self._foundNode = self._array[self._index]
        while self._foundNode != None:
            if self._foundNode.data == item: 
                return True
            else:
                self._priorNode = self._foundNode
                self._foundNode = self._foundNode.next
        return False

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"
    
    def printChains(self):
        """
        Prints out each array cell with it's chain. 
        """
        for node in self._array:
            if node != None: 
                print(node.data, end = " ")
                head = node
                while head.next != None:
                    head = head.next
                    print(head.data, end = " ")
                print()
            else:
                print("None")

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self._array):
            node = self._array[cursor]
            while node != None:
                yield node.data
                node = node.next
            cursor += 1

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._loadedCells = 0
        self._array = Array(HashSet.DEFAULT_CAPACITY)

    def add(self, item):
        """Adds item to self. If index is already occupied, add to front of the chain."""
        if not item in self: # __contains__
            
            # Add to new cell and keeps track of how many cells are occupied
            if self._array[self._index] == None:
                self._array[self._index] = Node(item,
                                                self._array[self._index])
                self._size += 1
                self._loadedCells += 1
                
                # Every time a new cell is taken, determine if we need to rehash()
                if self.loadFactor() > 0.8:
                    self.rehash()
            else:
                # This adds the new item to the chain
                self._array[self._index] = Node(item,
                                                self._array[self._index])
                self._size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        if not item in self:
            raise KeyError(str(item) + " not in set")
        elif self._priorNode == None:
            self._array[self._index] = self._foundNode.next
        else:
            self._priorNode.next = self._foundNode.next
        self._size -= 1 

    # Utility methods
    def loadFactor(self):
        """
        Computes (total items) / (array capacity)
        """
        return len(self) / len(self._array)
    
    def cellLoadFactor(self):
        """
        Computes (total filled cells) / (array capacity)
        """
        return self._loadedCells / len(self._array)

    def rehash(self):
        """
        This method multiplies the length of array's capacity by two,
        and redistributes the items. Chain lengths will be reduced. 
        """
        items = list(self)
        self._array = Array(len(self._array) * 2)
        self._size = 0
        self._loadedCells = 0 
        for item in items:
            self.add(item)

def main():

    hset1 = HashSet([1,2,3,4,7,8,10,12])
    hset1.printChains()
    print("cellLoadFactor = ", hset1.cellLoadFactor())
    print("_"*70)
    
    hset1.add(9) #9 gets added to chain
    hset1.add(14)
    hset1.add(30)
    hset1.printChains()

#    print("cellLoadFactor = ", hset1.cellLoadFactor())
#    print("_"*70)
#    hset1.rehash()
#    hset1.printChains()
    
if __name__ == "__main__":
    main()
