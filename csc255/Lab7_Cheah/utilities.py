'''
Ricky Cheah
Lab 7
Utility function module
'''
def main():
    pass

def compareFiles(inputFile, decodedFile):
    '''
    This function takes in the original @inputFile and compares it to the final @decodedFile.
    File lengths and specific data indices are checked.
    Raises RuntimeError if disprepancies are found. 
    '''
    fin = open(inputFile, 'rb')
    fdecoded = open(decodedFile, 'rb')
    
    bufferCount = 0
    blockSize = 1024 # we check 1024 bytes each loop from each of the two files. 
    buffer1 = fin.read(blockSize)
    buffer2 = fdecoded.read(blockSize)
    while buffer1 and buffer2:
        if len(buffer1) != len(buffer2):
            raise RuntimeError("Sizes of the files are different!\n" + \
                               f"{inputFile} has size {bufferCount*blockSize + len(buffer1)} but " + \
                               f"{decodedFile} has size {bufferCount*blockSize + len(buffer2)}.")
        for i in range(min(len(buffer1), len(buffer2), 1024)):
            if buffer1[i] != buffer2[i]:
                raise RuntimeError(f"files have different data at position {bufferCount*blockSize + i}!\n" +
                                   f"{inputFile} has '{chr(buffer1[i])}' at index {i}, but {decodedFile} has '{chr(buffer2[i])}'.")

        buffer1 =  fin.read(blockSize) # continues on to next block of bytes
        buffer2 = fdecoded.read(blockSize)
        bufferCount += 1 # keep track of how many blocks we checked. 

def bytePresentation(byte):
    '''
    helper function to print/display the bytes properly. 
    '''
    if byte == b'\n': return "\\n"
    if byte == b'\r': return "\\r"
    if byte == b'\t': return "\\t"
    
    if byte >= b' ' and byte <= b'~':
        return str(f"'{byte.decode('utf-8')}'")
    
    else:
        return f"0x{byte.hex()}"

class BlockReader(object):
    '''
    Class to aid in the reading of data from streams. 
    '''
    def __init__(self, f_object, count, debugObject):
        self._count = count # this many bytes per read.
        self._inputStream = f_object
        self.debugObject = debugObject
    
    def dataRemains(self):
        '''
        This attempts to read one byte of data, and if that is possible,
        this means that there are more data to be read. Cursor is shifted back one step.
        '''
        if self._inputStream.read(1):
            self._inputStream.seek(-1,1)
            return True
        return False # EOF
    
    def readData(self):
        '''
        Reads a specific amount of bytes from the inputStream each time this method is called.
        resets count.
        using bitwise operations, new data is added to the right end of bigNumber. 
        '''
        count = self._count
        width = 0 # this keeps track of how many bytes of data are in bigNumber
        bigNumber= 0
        self.debugObject.write(f"BigNumberReader::readData - Requested count {self._count} bytes, got\n")
        
        while count:
            byte = self._inputStream.read(1)
            if not byte: # EOF
                break

            bigNumber = (bigNumber << 8) # shifts bigNumber by one byte (0xff) so we get 0xff00
            bigNumber = bigNumber | ord(byte) # the new data gets added to the 00 portion. 

            self.debugObject.write(f"[{width}] {bytePresentation(byte)} ")
            count -= 1
            width += 1
        
        self.debugObject.write(f"\nBigNumberReader::readData - Read {hex(bigNumber)} as {width} bytes\n\n")
        return (bigNumber, width) 

class BlockWriter(object):
    '''
    This block writer class aids the conversion of a big number back to characters
    using bitwise operations. 
    '''
    def __init__(self, f_object, debugObject):
        self._outputStream = f_object
        self.debugObject = debugObject

    def dataRemains(self):
        '''
        This attempts to read one byte of data, and if that is possible,
        this means that there are more data to be read. Cursor is shifted back one step.
        '''
        if self._f_object.read(1):
            self._f_object.seek(-1,1)
            return True
        return False
    
    def writeData(self, decryptedNumber, blockLength):
        '''
        This method aids in the conversion of a big number back into characters.
        the blockLength input indicates the number of characters that 
        decryptedNumber represents. 
        '''
        oneByte = 8
        shiftIndex = blockLength-1
        
        self.debugObject.write(f"BlockWriter::writeData - Writing {hex(decryptedNumber).upper()} as {blockLength} bytes\n")
        while shiftIndex > -1:
            # first we shift the number right so the data we want is the first 8 bits.
            # the & AND operation masks everything else out except the 8 bits we want.
            number = (decryptedNumber >> oneByte*(shiftIndex)) & (0b11111111)

            byte = number.to_bytes(1, byteorder = 'little') # converts int to byte
            self.debugObject.write(f"[{blockLength-(shiftIndex+1)}] {bytePresentation(byte)} ")
            self._outputStream.write(byte)
            shiftIndex  -= 1
        self.debugObject.write(f"\n\n")


if __name__ == "__main__":
    main()