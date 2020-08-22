'''
Ricky Cheah
Lab 6
7/17/2020

HuffmanCodec Class
'''
from huffmanalgorithm import HuffmanAlgorithm 

class HuffmanCodec(object):
    '''
    This class serves to communicate between the Driver file and the HuffmanAlgorithm class.
    Input, output, and debug file objects are sent as input to methods here, and are then
    passed to appropriate HuffmanAlgorithm methods to complete the encoding and decoding. 
    '''

    # PRIVATE #
    def __init__(self):
        self._huffmanAlgorithm = HuffmanAlgorithm() # 
        
    def makeFrequencyTable(self, fin, debugObject):
         '''
         This method loops through the input file for the first time, and creates a
         frequency table based on the number of occurences of the characters. 
         Each byte will be sent to HuffmanAlgorithm to be counter and stored in a table.
         '''
         self._huffmanAlgorithm.initFrequencyTable() 
         
         byte = fin.read(1)
         
         while byte:
             self._huffmanAlgorithm.countCharacters(byte)
             byte = fin.read(1)
         self._huffmanAlgorithm.printFrequency(debugObject)
         
        
    def encodeData(self, fin, fout):
         '''
         This methods loops through input file for the second, after we have made our
         frequency table, and encoding table.
         Each byte read will be encoded according to the encoding table, and then written
         to the output encoded file. 
         '''

         fin.seek(0) # resets cursor since previously have read till the end
         byte = fin.read(1)

         while byte:
             singleEncoded = self._huffmanAlgorithm.outputEncoded(byte)
             fout.write(singleEncoded)
             byte = fin.read(1)
    
    def decodeData(self, fin, fout): # initFrequencyTable(self)
        '''
        This method loops through our encoded file, and for each byte it encounters, it tries
        to decode it back to character form. 
        '''
        byte = fin.read(1)
        while byte:
            ch = self._huffmanAlgorithm.inputDecoded(byte)
            if ch:
                fout.write(ch)
            byte = fin.read(1)
            
    # PUBLIC #
             
    def encodeStream(self, fin, fout, debugObject):
        '''
        This method receives all the file objects from driver and calls the appropriate 
        privatemethods to build a frequency table, an encoding table, and finally encode 
        the original input data. 
        '''
        self.makeFrequencyTable(fin, debugObject)
        self._huffmanAlgorithm.buildHuffmanTree(debugObject)
        self._huffmanAlgorithm.makeEncodingTable(debugObject)

        self.encodeData(fin, fout)
    
    def decodeStream(self, fin, fout):
        '''
        This method calls a private method to loop through encoded data to decode it. 
        '''
        self.decodeData(fin, fout)
                     