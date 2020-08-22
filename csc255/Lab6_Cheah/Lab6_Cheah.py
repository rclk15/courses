'''
Ricky Cheah
Lab 6
7/17/2020

Driver File
'''
from huffmancodec import HuffmanCodec

def main():

    for i in range(1,12):
        try:
            print(f"*** Testing file {i}_in.txt, debug output file {i}_debug.txt ***\n")
            testFile(i)
            print("OK\n")

        except RuntimeError as err:
            print(err.args[0])
    
def testFile(numberFile):
    huffmanCodec = HuffmanCodec() # class that will relay information to HuffmanAlgorithm
   
    inputFile = f"{numberFile}_in.txt"
    encodedFile = f"{numberFile}_encoded.txt"
    decodedFile = f"{numberFile}_decoded.txt"
    debugFile = f"{numberFile}_debug.txt"
    
    debugObject = open(debugFile, 'w') # progress will be stored here for debugging

    testEncoding(huffmanCodec, inputFile, encodedFile, debugObject)
    testDecoding(huffmanCodec, encodedFile, decodedFile, debugObject)
    
    compareFiles(inputFile, decodedFile) # comparing original input file and final decoded file
    debugObject.write(f"!!! {inputFile} and {decodedFile} are equal.")

    debugObject.close()

def compareFiles(inputFile, decodedFile):
    '''
    This function takes in the original @inputFile and compares it to the final @decodedFile.
    File lengths and specific data indices are checked.
    Raises RuntimeError if disprepancies are found. 
    '''
    fin = open(inputFile, 'rb')
    fdecoded = open(decodedFile, 'rb')
    
    '''
    Start Error checkers: deliberately adding discrepancies. Uncomment the code below to try.
    '''
#    fdecoded = open(decodedFile, 'rb+') #open file in read and write mode so we can alter it.
#    # length error checker
#    fdecoded.write(b'x'*30)   
#    fdecoded.seek(0)
#    
#    # character error checker
#    fdecoded.write(b'x')   
#    fdecoded.seek(0)
    '''
    End Error checkers.
    '''
    
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

    
def testEncoding(huffmanCodec, inputFile, encodedFile, debugObject):
    '''
    This function opens the input file and the file to be filled with encoded data, 
    and passes the file objects to the huffmanCodec to be encoded.
    @debugObject is passed so progress be recorded.
    '''
    try:
        fin = open(inputFile, 'rb') 
    except:
        raise RuntimeError(f"could not open {inputFile} in testEncoding()")
    
    try:
        fout = open(encodedFile, 'w') 
    except:
        raise RuntimeError(f"could not open {encodedFile} in testEncoding()")
        
    debugObject.write(f"Encoding {inputFile} -> {encodedFile}\n\n")
    
    huffmanCodec.encodeStream(fin, fout, debugObject)
    
    fin.close()
    fout.close()

def testDecoding(huffmanCodec, encodedFile, decodedFile, debugObject):
    '''
    This function opens the previously encoded file, and passes the file objects
    into huffmanCodec so we can try to decode the data within using the HuffmanTree 
    currently stored in a heap object (previously created during encoding in HuffmanAlgorithm). 
    @debugObject is passed so progress be recorded.
    '''
    
    try:
        fencoded = open(encodedFile, 'rb') # byte 
    except:
        raise RuntimeError(f"could not open {encodedFile} in testDecoding()")
    try:
        fdecoded = open(decodedFile, 'wb')
    except:
        raise RuntimeError(f"could not open {decodedFile} in testDecoding()")

    debugObject.write(f"\nDecoding {encodedFile} -> {decodedFile}\n\n")
    huffmanCodec.decodeStream(fencoded, fdecoded)
    
    fencoded.close()
    fdecoded.close()


if __name__ == "__main__":
    main()