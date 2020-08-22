"""
Ricky Cheah
7/4/2020
Heap Class (Modified for use with KruskalMST for Lab 5)
"""

class Heap(object):
    '''
    Heap Class that maintains a min-heap of tuples according to the tuples' [0]
    '''
    
    def __init__(self, data = []):
        '''
        data: an iterable containing comparables.
        Initialize size and list to store elements.
        Uses insert() to maintain a consistent min-heap.
        '''
        self._heapList = []
        self._size = 0
        for item in data:
            self.insert(item)
            
    def __str__(self):
        '''
        Shows the heap without comma and square brackets.
        '''
        return ' '.join(map(str, self._heapList))
    
    def __bool__(self):
        '''
        Returns True if heap is not empty.
        '''
        return self._size > 0
    
    def percolateUp(self, comparable: int):
        '''
        Modified: We are compating the [0] index of a tuple.
        
        comparable: the newly inserted element.
        This method is called when inserting new elements.
        Start with the last index of the heap, compares values with parent.
            If parent is larger, values are swapped, and index is updated.
        '''
        currentIndex = self._size - 1
        parentIndex = (currentIndex - 1) // 2
#        print(comparable)
#        print(self._heapList)
        # keep checking until parentIndex == 0.
        # (currentIndex != parentIndex) is for when self._size == 1. 
        while parentIndex > -1 and currentIndex != parentIndex :
            parentValue = self.getElement(parentIndex)
            if parentValue[0] > comparable[0]:
#                print(parentValue[0] ,comparable[0])
                self.swap(currentIndex, parentIndex)
                currentIndex = parentIndex # updates current index and parent index
                parentIndex = (currentIndex - 1)//2
#                print(self._heapList)
            else:
                return
        return
                

    def percolateDown(self, comparable):
        '''
        Modified: We are compating the [0] index of a tuple.
        
        comparable: the element just moved to index 0.
        This method is used to aid deleteMin().
        After the last element takes the 0 index position, percolateDown()
        compares its value with its left & right child and swaps to maintain min-heap.
        '''
        currentIndex = 0
        
        
        while currentIndex*2 + 1 < self.size() : # makes sure at least have LEFT child.
            leftChildIndex = currentIndex*2 + 1
            leftChild = self.getElement(leftChildIndex) 
            
            # this portion finds the smallest child to compare with.
            rightChildIndex = currentIndex*2 + 2
            if rightChildIndex < self.size(): # making sure right child is available
                rightChild = self.getElement(rightChildIndex) 
                
                if leftChild[0] > rightChild[0] or leftChild[0] == rightChild[0]:
    #                print("smallest", leftChildIndex )
                    smallestChildIndex = rightChildIndex
                else:
                    smallestChildIndex = leftChildIndex
            else: # no right child, so left is used to compare.
                smallestChildIndex = leftChildIndex
                
#            print(self.getElement(currentIndex), leftChild, rightChild)
            
                
            if comparable[0] > self.getElement(smallestChildIndex)[0]:
                self.swap(currentIndex, smallestChildIndex)
                currentIndex = smallestChildIndex 
            else:
                return

    def insert(self, item):
        '''
        This method inserts a new element at the last position of the heap.
        Uses percolateUp() to maintain min-heap.
        '''
        self._heapList.append(item) #need to percolateUp this item, len-1 index
        self._size += 1
        self.percolateUp(item)
        
    
    def deleteMin(self):
        '''
        Pops and returns the element at index 0, the minimum value.
        Moves the last item of the heap to index 0.
        Uses percolateDown() on the new index 0 item to maintain min-heap.
        '''
        self.swap(0, self.size()-1)
        minimum = self._heapList.pop()
        self._size -= 1
        if self.size():
            self.percolateDown(self._heapList[0]) #This gives the tuple at [0]
        return minimum
    
    def getElement(self, index: int):
        '''
        Returns the element at @index location of heap.
        '''
        return self._heapList[index]
    
    def swap(self, position1: int, position2: int):
        '''
        Swaps the two values at location @position1 and @position2
        '''
        self._heapList[position1], self._heapList[position2] = \
            self._heapList[position2], self._heapList[position1]
        return
    
    def size(self):
        '''
        Returns the current size of the heap.
        '''
        return self._size
        
