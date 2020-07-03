'''
Ricky Cheah
Mar 5, 2020

This is an abstract bag class meant to be the parent class for other bag classes. 
'''


class AbstractBag(object):
    
    #TRACE = True will print out where a function is called
    TRACE = False;
    
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        
        if self.TRACE:
            print("abstractbag's __init__")
        
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    
    def __str__(self):
        """Returns the string representation of self."""
        
        if self.TRACE:
            print("abstractbag's __str__")
            
        return "{" + ", ".join(map(str, self)) + "}"
    
    def __len__(self):
        """-Returns the number of items in self."""
        
        if self.TRACE:
            print("abstractbag's __len__")
            
        return self._size
    
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        
        if self.TRACE:
            print("abstractbag's isEmpty")
            
        return len(self) == 0

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        
        if self.TRACE:
            print("abstractbag's __add__")
            
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        
        if self.TRACE:
            print("abstractbag's __eq__")
            
        if self is other: return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False
        for item in self:
            if not item in other:
                return False
        return True

    def clone(self):
        """
        When called on an existing Bag object, returns an exact copy.
        Note: items in cloned linkedBag will be in reverse order.
        """
        if self.TRACE:
            print("abstractbag's clone")

        return type(self)(self) #this creates the same type of bag that the method was called on. 