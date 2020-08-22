'''
Ricky Cheah
Lab 6
7/17/2020

HuffmanTree Class
'''

class HuffmanTree(object):
    '''
    This class contains all the methods to create/merge huffman trees and methods to
    retrieve data from them. 
    '''
    def __init__(self, input1, input2):
        self._decodeCursor = self # keep track of current path position when decoding. 
        
        # __init__ 1: creates a single huffman tree
        if type(input1) == bytes and type(input2) == int:
            self._byte = input1
            self._frequency = input2
            
            self._left, self._right = None, None
            
        # __init__ 2: merges two huffman trees. 
        elif type(input1) == HuffmanTree and type(input2) == HuffmanTree:
            self._byte = None # the merged tree won't have a byte/character. 
            # adding the frequencies of the two trees together.
            self._frequency = input1._frequency + input2._frequency 
            if input1._frequency <= input2._frequency: 
                self._left, self._right = input1, input2 
            else:
                self._left, self._right = input2, input1
        else:
            raise RuntimeError(f"HuffmanTree takes in either: a byte and a frequency, or two HuffmanTree instances")

    def __str__(self):
        '''str representation'''
        if self._byte:
            return f"[{self._frequency}, {self._byte}]"
        elif self._left and self._right:
                return f"[{self._frequency}, {self._left}, {self._right}]"
    
    def __repr__(self):
        '''repr representation'''
        return self.__str__()
    
    def getFrequency(self) -> int:
        '''
        returns the frequency of a byte/character or the combined frequency on the merged tree. 
        '''
        return self._frequency
    
    def getByte(self) -> bytes: 
        '''returns the byte/ch stored at current tree'''
        return self._byte
    
    def resetCursor(self):
        '''
        resets decodeCursor to the root of the tree. 
        '''
        self._decodeCursor = self
        return self._decodeCursor
    
    def cursorLeft(self):
        '''
        moves the tracking cursor down the left child. If that child is a leaf, 
        its byte/character will be returned. 
            Else, the position of the child gets returned, and the process continues.
        '''
        leftTree = self.getLeft()
        if leftTree: # This catches edge case: only one type of character in document.
            if leftTree.isTerminal():
                returnedCharacter = leftTree.getByte()
                return (True, returnedCharacter)
            return (False, self.getLeft())
        else:
            return (True, self.getByte())

    def cursorRight(self):
        '''
        Similar to cursorLeft()
        '''
        rightTree = self.getRight()
        if rightTree.isTerminal():
            returnedCharacter = rightTree.getByte()
            return (True, returnedCharacter)
        return (False, self.getRight())
        
    def getLeft(self) -> 'HuffmanTree':
        '''
        returns the left child
        '''
        return self._left
    
    def getRight(self) -> 'HuffmanTree':
        '''
        returns the right child
        '''
        return self._right
    
    def isTerminal(self) -> bool:
        '''
        Returns True if the current tree is a leaf (has no left or right child.)
        '''
        return not self._right and not self._left

