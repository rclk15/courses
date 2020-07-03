"""
Ricky Cheah
4/27/2020

File: hashtable.py

Original Author: Ken Lambert
"""

from arrays import Array

class HashTable(object):
    "Represents a hash table."""

    EMPTY = None
    DELETED = True

    def __init__(self, capacity = 10,
                 hashFunction = hash,
                 linear = True):
        self._table = Array(capacity, HashTable.EMPTY)
        self._size = 0
        self._hash = hashFunction
        self._homeIndex = -1
        self._linear = linear
        self._probeCount = 0
    
    def __contains__(self, item): # used also in get(), insert() and remove()
        self._homeIndex = abs(self._hash(item)) % len(self._table)
        distance = 1
        self._containsIndex = -1 # this keeps track of the item looked for
        index = self._homeIndex
        
        # this keeps looking until we find the item, or reach and empty cell. 
        while not self._table[index] in (HashTable.EMPTY,
                                         HashTable.DELETED, item):
            
            # Increment the index and wrap around to first 
            # position if necessary
            if self._linear:
                increment = index + 1
            else:
                # Quadratic probing
                increment = self._homeIndex + distance ** 2
                distance += 1
            index = increment % len(self._table)
        
        # check where while loop stopped to see if we found item
        if self._table[index] == item:
            self._containsIndex = index # record the item's location
            return True
        return False
    
    def get(self,item):
        """
        This method returns the index of the item, or -1 if item is not in table. 
        """
        item in self #this runs __contains__ to set self._containsIndex
        return self._containsIndex
    
    def remove(self,item):
        """
        This method returns True if item is removed successfully,
            or -1 if item is not in table thus can't be removed. 
        """
        if item in self:
            self._table[self._containsIndex] = HashTable.DELETED
            self._containsIndex = -1 # resets containsIndex
            return True
        else:
            return self._containsIndex
            
    def insert(self, item):
        """Inserts item into the table
        Preconditions: There is at least one empty cell or
        one previously occupied cell.
        There is not a duplicate item."""
        self._probeCount = 0
        # Get the home index
        self._homeIndex = abs(self._hash(item)) % len(self._table)
        distance = 1
        index = self._homeIndex

        # Stop searching when an empty cell is encountered
        while not self._table[index] in (HashTable.EMPTY,
                                         HashTable.DELETED):
            
            if  self._table[index] == item:
                print(item, "already exist in table.")
                break
            # Increment the index and wrap around to first 
            # position if necessary
            if self._linear:
                increment = index + 1
            else:
                # Quadratic probing
                increment = self._homeIndex + distance ** 2
                distance += 1
            index = increment % len(self._table)
            self._probeCount += 1

            
        # An empty cell is found, so store the item
        self._table[index] = item
        self._size += 1
        self._actualIndex = index

    
    def actualIndex(self):
        return self._actualIndex
    
    def homeIndex(self):
        return self._homeIndex
    
    def probeCount(self):
        return self._probeCount
    
    def loadFactor(self):
        return self._size / len(self._table)
    
    def __str__(self):
        return str(self._table)
    
def main():
    # linear probing
    table1 = HashTable()
    table1.insert(3) # index 3
    table1.insert(4) # index 4
    table1.insert(13) # probes from 3, 4, to index 5
    print(f"Home for 13 is {table1._homeIndex}, probeCount = {table1._probeCount}")
    table1.insert(9) 
    print(table1)
    print("Current loadFactor =", table1.loadFactor())
    table1.insert(3) # insert duplicate
    print(3 in table1) # search for existing item (__contains__)
    print(6 in table1) # search for non-existing item (__contains__)
    print("get(3) =", table1.get(3)) # get index for existing item
    print("get(3) =", table1.get(6)) # get index for non-existing item
    print("remove(3) =", table1.remove(3)) # remove existing item  
    print("remove(10) =", table1.remove(10))  # remove non-existing item
    print(table1)            
    
    print("_"*60)
    
    # quadratic probing
    table2 = HashTable(10, hash, False)
    table2.insert(3) # index 3
    table2.insert(4) # index 4
    table2.insert(7) # index 7
    table2.insert(13) # probe wraps around from index 3, 4, 7 to index 2
    print(f"Home for 13 is {table2._homeIndex}, probeCount = {table2._probeCount}")
    print(table2)
    print("Current loadFactor =", table2.loadFactor())
    print("get(3) =", table2.get(3)) # get index for existing item
    print("get(3) =", table2.get(6)) # get index for non-existing item
    print("remove(3) =", table2.remove(3)) # remove existing item  
    print("remove(10) =", table2.remove(10))  # remove non-existing item
    print(table2)   


if __name__ == "__main__":
    main()


