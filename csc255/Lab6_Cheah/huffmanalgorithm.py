'''
Ricky Cheah
Lab 6
7/17/2020

HuffmanAlgorithm Class
'''

from heap import Heap 
from huffmantree import HuffmanTree
from utilities import bytePresentation
    
class HuffmanAlgorithm(object):
    '''
    This class contains all the necessary functions to encode and decode data, along
    with assistive functions to build frequency table and encoding table. 
    ''' 

    # PUBLIC #

    def countCharacters(self, byte):
        '''
        For each byte this method receives, it updates the frequency in the freqencytable.
        '''
        if ord(byte) in self._frequencyTable:
            self._frequencyTable[ord(byte)][1] += 1
        else:
            self._frequencyTable[ord(byte)] = [byte, 1]
    
    def buildHuffmanTree(self, debugObject):
        '''
        This methods builds a single node huffmantree for all elements in the sortedTable,
        then inserts them into a heap.
        It then repeatedly removes the 2 least frequency nodes in the heap and merge them,
        until we are left with one final huffmantree. 
        '''
        for item in self._sortedTable:
            if item:
                self._heap.insert(HuffmanTree(item[1][0], item[1][1])) # creating single trees. 
        self.printQueue(debugObject)

        while(self._heap.size() > 1):

            min1 = self._heap.deleteMin()
            min2 = self._heap.deleteMin()
            self._heap.insert(HuffmanTree(min1, min2)) # merging two trees. 
        
    def makeBitData(self, tree):
        '''
        This method starts the process of finding the encoding for each character. 
        '''
        left = tree.getLeft()
        right = tree.getRight()

        if left:
            self.makeTreeBitData(left, "0")
        if right:
            self.makeTreeBitData(right, "1")
        if not left and not right:
            self.makeTreeBitData(tree, "0")
    
    def makeTreeBitData(self, tree, currentPath):
        '''
        This method uses recursion to go down the branches of the tree, depending on
        whether 1 or 0 is received, until it reaches a leaf, and the path to get to that leaf
        is the encoding for the leaf's character. 
        '''
        left = tree.getLeft()
        right = tree.getRight()
        if left:
            self.makeTreeBitData(left, currentPath + "0")
        if right:
            self.makeTreeBitData(right, currentPath + "1")
        else:
            byte = tree.getByte()
            self._encodingTable[ord(byte)] = (byte, currentPath)
    
    def outputEncoded(self, byte):
        '''
        This method looks up the corresponding encoding for the input byte.
        '''
        return self._encodingTable[ord(byte)][1]
    
    def inputDecoded(self, byte):
        '''
        This method goes down the huffman tree until it reaches a leaf, and returns the 
        character in the leaf.
        There is a cursor in the huffman tree that keeps track our current path in the tree.
        '''
        tree = self._heap._heapList[0]
        currentCursor = tree._decodeCursor
        decodedCharacter = None
         
        if byte == b'0': 
            decodedCharacter = currentCursor.cursorLeft()

        elif byte == b'1':
            decodedCharacter = currentCursor.cursorRight()

        if decodedCharacter[0]: # we have reach a leaf and found a character. 
            currentCursor = tree.resetCursor() # Cursor (of root) is reset to point to itself. 
            return decodedCharacter[1]
        else: 
            tree._decodeCursor = decodedCharacter[1] # this moves the cursor forward. 
            return None

    
    def makeEncodingTable(self, debugObject):
        '''
        This method uses our completed huffman tree to create table containing all the encoding
        for the characters in our frequency table. 
        '''

        debugObject.write(f"\nmakeBitData:\n\n")
        if self._heap._heapList: # this catches empty file.
            completedTree = self._heap._heapList[0] # this is the merged tree, there is only one. 
            self._encodingTable = {}
            self.makeBitData(completedTree)
        
            for item in sorted(self._encodingTable.items()): # writing to debug file. 
                debugObject.write(f"{str(item[0]).ljust(4)} {bytePresentation(item[1][0]).ljust(4)}  {{{item[1][1]}}}\n")

    # PRIVATE #
    
    def initFrequencyTable(self):
        '''
        This initializes a dictionary to serve as a frequency table, and a priority(min heap)
        queue for creating our final huffman tree later.
        '''
        self._frequencyTable = {}
        self._heap = Heap()
    
    def printFrequency(self, debugObject):
        '''
        After our frequency table has been completed, this method sorts the table by 
        their ASCII code and writes them to the debugging file. 
        '''
        self._sortedTable = sorted(self._frequencyTable.items(), reverse = False)
        debugObject.write(f"countCharacters: \n\n")
        for item in self._sortedTable:
            debugObject.write(f"{str(item[0]).ljust(4)} {bytePresentation(item[1][0]).ljust(4)}  {{{item[1][1]}}}\n")
        
    def printQueue(self, debugObject):
        '''
        This method creates a deep copy of our min heap, and each time deletes the minimum
        and writes it to the debugging file to show the order of the queue. 
        '''
        tempHeap = Heap() 
        tempHeap._heapList = self._heap._heapList[:] # creates copy
        tempHeap._size = self._heap._size # copies the size
        debugObject.write(f"\nprintQueue: \n\n")

        while(tempHeap._heapList):

            minimum = tempHeap.deleteMin()
            byte = minimum.getByte()
            freq = minimum.getFrequency()

            debugObject.write(f"{str(ord(byte)).ljust(4)} {bytePresentation(byte).ljust(4)} {{{freq}}}\n")

