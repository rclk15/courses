"""
Ricky Cheah
7/10/2020
Partition Class

Written by referencing original code by:
    Goodrich, Tamassia and Goldwasser. 
"""
    
class Partition(object):
    '''
    Helper class for KruskalMST.
    Assist with the creation of sub-graphs,
    keeping track of node relations and and union of sub-graphs.
    '''
    # ---------------Partition() Private ---------------
    
    # Note position is not actually stored in Partition()
    class Position(object):
        '''
        Storange class to store information of each node. 
        '''
        __slots__ = '_container', '_element', '_size', '_parent'
    
        def __init__(self, container, element):
            self._container = container # the partition instance
            self._element = element
            self._size = 1
            self._parent = self
            
        def __str__(self):
            '''
            returns the str of element.
            '''
            return str(self._element)
        
        def __repr__(self):
            '''
            returns the str of current parent of the position.
            Utilized when printing a Position dictionary value.
            '''
            return str(self._parent)
        
        def element(self):
            '''
            returns the element stored in this position
            '''
            return self._element
        
    # ---------------Parition() Public ---------------
    
    def createGroup(self, element):
        '''
        This creates a single node sub-graph with a provided node/element. 
        '''
        return self.Position(self, element)
    
    def findParent(self, position):
        '''
        This finds the highest level parent of a position. 
        '''
        if position._parent != position:
            # this uses path compression
            # updates node's parent to the highest level parent each recursion. 
            position._parent = self.findParent(position._parent)
        return position._parent
    
    def positionUnion(self, position1, position2):
        '''
        This merges sub-graphs by assigning the larger sub-graph as the 'parent'
        of the smaller sub-graph. 
        '''
        parent1 = self.findParent(position1)
        parent2 = self.findParent(position2)
#        print(parent1, parent2)
        if parent1 is not parent2: # this if might be redundant, since we checked in KruskalMST final while loop
            if parent1._size > parent2._size:
#                print(parent2._parent)
                parent2._parent = parent1
#                print(parent2._parent)
                parent1._size += parent2._size
            else:
                parent1._parent = parent2
                parent2._size += parent1._size                


def main():
    partition1 = Partition()
    position1= partition1.createGroup('abc')
    print(partition1)
    print(position1) # this uses __str__
    print(position1._parent)
    position1._parent = 'def'
    print(position1._parent)
    dictionary1 = {}
    dictionary1['abc'] = position1
    print(dictionary1) # this uses __repr__ 
    
    print

if __name__ == "__main__":
    main()
