"""
Ricky Cheah
6/26/2020
Lab 3 
DoubleHashingProbingHash Class
"""

from hashbase import HashBase

class DoubleHashingProbingHash(HashBase):
    '''
    This hash table class uses double hashing probing and extends the HashBase class.
    '''

    def __init__(self, initialSize, doubleFactor):
        '''
        Initializes using HashBase class. 
            self._table = [None]*initialSize
            self._collisions = 0
            self._inserted = 0
        self.doubleFactor for use in secondary hashing. 
        '''
        HashBase.__init__(self, initialSize)
        self.doubleFactor = doubleFactor
    
    def lookUp(self, key: int):
        '''
        This method uses double hashing to find the index based on the hashed key.
        Secondary hashed value is added to original hashed value if collision occurs.
        The index location could be empty, or could already contains the existing key.
        '''
        startIndex = self.hashIndex(key)
        index = startIndex
        
        factor = 1 # secondary hash multiplication factor.
        firstHash = self.hashFunction(key)
        secondHash = self.doubleFactor - (firstHash % self.doubleFactor)
        
        while True:
            p = self._table[index]
            if p  == None or p._key == key: # found empty slot, or key already exist.     
                return index
            self._collisions += 1

            index = startIndex # reverting to the start index. 
            index += factor*secondHash    

            index %= len(self._table)
            factor += 1
            
            if index == startIndex: # index has completely circled around _table.
                return len(self._table) + 1 # this shows that table is full or a circular hash. 
            
