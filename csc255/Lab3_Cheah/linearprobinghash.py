"""
Ricky Cheah
6/26/2020
Lab 3 
LinearProbingHash Class
"""

from hashbase import HashBase

class LinearProbingHash(HashBase):
    '''
    This hash table class uses linear probing and extends the HashBase class.
    '''

    def __init__(self, initialSize):
        '''
        Initializes using HashBase class. 
            self._table = [None]*initialSize
            self._collisions = 0
            self._inserted = 0
        '''
        
        HashBase.__init__(self, initialSize)
    
    def lookUp(self, key: int):
        '''
        This method uses linear probing to find the index based on the hashed key.
        The index location could be empty, or could already contains the existing key.
        '''
        startIndex = self.hashIndex(key)
        index = startIndex 

        while True:
            p = self._table[index]
            if p  == None or p._key == key: # found empty slot, or key already exist.
                return index

            self._collisions += 1
            index += 1   
            index %= len(self._table)

            if index == startIndex: # index has completely circled around _table.
                return len(self._table) + 1 # this shows that table is full or circular hash
            
