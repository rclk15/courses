"""
Ricky Cheah
6/26/2020
Lab 3 
QuadraticProbingHash Class
"""

from hashbase import HashBase

class QuadraticProbingHash(HashBase):
    '''
    This hash table class uses quadratic probing and extends the HashBase class.
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
        This method uses quadratic probing to find the index based on the hashed key.
        The index location could be empty, or could already contains the existing key.
        '''
        startIndex = self.hashIndex(key)
        index = startIndex
        
        base = 1 # This is the base of the soon to squared value. 

        while True:
            p = self._table[index]
            if p  == None or p._key == key: # found empty slot, or key already exist.     
                return index
            self._collisions += 1
            
            index = startIndex # Reverting to start index 
            index += base**2 # Quadratic probing
            index %= len(self._table)
            base += 1
            
            if index == startIndex: # index has completely circled around _table.
                return len(self._table) + 1 # this shows that table is full, or circular hash
            
