"""
Ricky Cheah
6/26/2020
Lab 3 
HashBase Class
"""

from hashinterface import HashInterface

class HashBase(HashInterface):
    '''
    Extends the HashInterface, and serves as a parent class for lower hash table classes.
    Lower classes will have different lookUp() method to probe the table. 
    '''
    
    # Private 
    
    class _Item(object):
        '''Lightweight composite to store key-value pairs'''
        __slots__ = '_key', '_value'
        
        def __init__(self, Key, Value):
            self._key = Key
            self._value = Value
            
        def __str__(self):
            return str(self._key) + " " + str(self._value)      
    
    def __init__(self, initialSize = 191):
        '''
        Constructor.
        '''
        self._table = [None]*initialSize
        self._collisions = 0 # Used to track number of collisions when using put()
        self._inserted = 0 # Track how many slots have been used in table
     
    def hashFunction(self, key: int):
        '''
        This method uses bitwise operations to hash the input key by scrambling it.
        '''
        return (key>>8)|((key & 0xff)<<16)
    

    def hashIndex(self, key: int):
        ''' 
        This calls hashFunction to hash key and obtains index.
        Returns the index value % table size. 
        '''
        index = self.hashFunction(key)
        return index % len(self._table)    
    
    # Public
    
    def get(self, key: int):
        '''
        This method uses lookUp() in lower classes to get the value associated with key in table.
        '''
        index = self.lookUp(key)
        
        if index > len(self._table) - 1:
            return None
        
        p = self._table[index]
        if p:
            return p._value
        else:
            return None
  
    def put(self, key: int, value: int):  
        '''
        This method uses lookUp() in lower classes to obtain an index and insert a key-pair into the table.
        '''        
        index = self.lookUp(key)
        if index > len(self._table) - 1 or self._inserted == len(self._table) : 
            raise RuntimeError("Table is full.")

        p = self._table[index]
        if p == None: # This sets the pair into an empty slot.
            self._table[index] = self._Item(key, value)
            self._inserted += 1
        else: # This overrides the previous value. 
            p._value = value
            
    def getCollisions(self):
        '''
        This method returns the total number of collisions recorded. 
        '''  
        return self._collisions