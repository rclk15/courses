"""
Ricky Cheah
7/4/2020
Lab 4
Driver File to test Heap class. 
"""
from heap import Heap

def main():
    
    # this tests in1.txt - in4.txt and creates corresponding output files. 
    # catches error if min-heap is not maintained
    for i in range(1, 5): 
        try:
            testFile(f"in{i}.txt", f"out{i}.txt")
        except RuntimeError as error:
            print(error)
def testFile(inFile: str, outFile: str):
    '''
    This function takes in @inFile and extracts its data into a list.  
    Opens @outFile in write mode and creates a file object with it. 
    '''
    data = readData(inFile)
    fileObject = open(outFile, 'w')
    testData(data, fileObject)
    fileObject.close()
    print(f"Input file:{inFile}, Output file:{outFile} Done.")

def readData(fileName: str) -> list:
    '''
    This function opens @fileName in read mode and extracts the int data into a list.
    '''
    f = open(fileName, 'r')
    data = list(map(int,f.read().split()))
    f.close()
    return data


def testData(data: list, fileObject):
    '''
    This function takes in a list of @data and a file object @fileObject
    Creates a new Heap instance with the list of @data, and verifies min-heap
    with checkHeap().
    Inserts some new values into the heap with insertOne(), and repeatedly remove
    the smallest item while maintaining heap using deleteOne().
    '''
    heap = Heap(data)
    printHeap("Heap", heap, fileObject)
    checkHeap(heap, fileObject)
    insertOne(heap, 31, fileObject)
    insertOne(heap, 14, fileObject)
    
    # This portion repeatedly removes the smallest element at the root. 
    while heap.size() > 0:
        
        # This portion changes the heap and should cause an error.
        # Uncomment this portion to test checkHeap()
        '''
        if heap.size() == 10:
            heap._heapList[7] = 4 # Error checker
        '''
        
        deleteOne(heap, fileObject) # this repeatedly remove smallest element. 

    
def insertOne(heap, element: int, fileObject):
    '''
    This function utilizes the @heap method insert() to insert a new @element.
    Verifies that it remains a min-heap afterwards.
    Writes resulting heap to @fileObject. 
    '''
    heap.insert(element)
    checkHeap(heap, fileObject)
    fileObject.write(f"Insert {element}\n")
    printHeap(f"Heap after insert {element}", heap, fileObject)


def deleteOne(heap, fileObject):
    '''
    This function utilies the @heap method deleteMin() to remove the element at
    the root of the heap. 
    Verifies that it remains a min-heap afterwards.
    Writes resulting heap to @fileObject.
    '''
    minimum = heap.deleteMin()
    checkHeap(heap, fileObject)
    fileObject.write(f"Delete min\n")
    printHeap(f"Heap after Delete min of {minimum}", heap, fileObject)
    
    if not heap.size():
        fileObject.write(f"Deleted all")

def checkHeap(heap, fileObject):
    '''
    This function utilizes checkElementOrder() and verifies that the heap is 
    ordered in a min-heap fashion, with each parent being smaller that its children.
    If not a min-heap, raises an error and prints error message to @fileObject.
    '''
    for i in range(heap.size()):

        if checkElementOrder(heap, i, i*2+1) and checkElementOrder(heap, i, i*2+2):
            continue
        else:
            printHeap("Not a heap.", heap, fileObject)
            fileObject.write(f"Error: heap violation at index {i}.\n" + \
                  f"parent,      heap({1}) = {heap.getElement(i)} \n" + \
                  f"left child,  heap({i*2 + 1}) = {heap.getElement(i*2+1)} \n" + \
                  f"right child, heap({i*2 + 2}) = {heap.getElement(i*2+2)} \n")
            fileObject.close()
            raise RuntimeError("Not a heap. Program exit.")
            

def checkElementOrder(heap, parentIndex: int, childIndex: int) -> bool:
    '''
    This function checks that the value at @parentIndex is smaller than that of
    the @childIndex. 
    '''
    if parentIndex > heap.size() - 1 or childIndex > heap.size() - 1 \
        or heap.getElement(parentIndex) <= heap.getElement(childIndex):
        return True
    return False


def printHeap(description: str, heap, fileObject):
    '''
    This function prints to @fileObject the @description, the current @heap size,
    and the current elements in the @heap.
    '''
    fileObject.write(f"{description}\nSize of heap: {heap.size()}\n{heap}\n\n") 

if __name__ == "__main__":
    main()
