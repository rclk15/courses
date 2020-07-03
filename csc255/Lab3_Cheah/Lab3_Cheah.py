"""
Ricky Cheah
6/26/2020
Lab 3 
Driver
"""

from linearprobinghash import LinearProbingHash
from quadraticprobinghash import QuadraticProbingHash
from doublehashingprobinghash import DoubleHashingProbingHash

# Global variables
tableSize = 191 # Prime number to reduce collisions
doubleFactor = 181 # The Prime number before tableSize. For use in DoubleHashingProbingHash.

def main():
    
    fileNames = [("in150.txt", "out150.txt"), ("in160.txt", "out160.txt"), ("in170.txt", "out170.txt")]
    
    for files in fileNames:
        try:
            testFile(files[0], files[1])
    
        except RuntimeError as error:
            print(error)
    
def testKeyValue(description: str, hashTable, key: int, value, outFile):
    '''
    This function takes a hashTable and inserts the key(int and value pair into the table. 
    The description describes the type of hashing function the table uses.
    Using the provided key, a value will be retrieved and compared to the provided value.
    The results and number of collisions(while attempting to insert) will be recorded to outFile. 
    
    Note: outFile is a pointer to an already opened file.
    Raises RuntimeError if the value retrieved is not the provided value. 
    '''
    
    previousCollision = hashTable.getCollisions()   
    hashTable.put(key, value)
    retrievedValue = hashTable.get(key)
    
    ''' This portion is only uncommented to test value mismatch's RuntimeError for in150.txt'''
#    if key == 1159:
#        retrievedValue = 2020
    ''' '''

    currentCollision = hashTable.getCollisions() - previousCollision 
    
    if retrievedValue == value: # retrieved value is correct.
        outFile.write(f"{key} : {value} -> {value}, collisions {currentCollision} \n")
    else: # also terminates function. 
        outFile.write(f"{key} : {value} -> {retrievedValue} Value mismatch! \n")
        outFile.close() 
        raise RuntimeError("put() and get() value mismatch! Run terminated.")


def testInputKey(key: int, lph, qph, dhph, outFile):
    '''
    Takes a key, and creates a value from the key.
    key, value and output file passed into three different hashTables.
    
    Note: outFile is a pointer to an already opened file.
    '''
    value = key*2

    testKeyValue("Linear   ", lph, key, value, outFile)
    testKeyValue("Quadratic", qph, key, value, outFile)
    testKeyValue("Double   ", dhph, key, value, outFile)
    outFile.write("\n")

def testData(description: str, data: list, outFilename: str):
    '''
    Creates three tables of different hashing strategies.
    description describes the state of data (sorted,ascending/sorted,descending/random)
    
    Takes the collection of input data, and passes them one by one as key into the tables.
    Opens the output file in append mode and passes the file pointer into testInputKey(). 
    '''

    lph = LinearProbingHash(tableSize)
    qph = QuadraticProbingHash(tableSize)
    dhph = DoubleHashingProbingHash(tableSize, doubleFactor)

    g = open(outFilename, 'a')
    g.write(f"***   {description} START   ***\n\n")
    for key in data:
        testInputKey(key, lph, qph, dhph, g)

    g.write(f"Linear       {lph.getCollisions()} collisions \n")
    g.write(f"Quadratic    {qph.getCollisions()} collisions \n")
    g.write(f"Double       {dhph.getCollisions()} collisions \n \n")
    g.write(f"***   {description} END   ***\n \n")
    g.close()


def readData(inFile):
    '''
    Opens a file and organizes the data into a list of ints and returns the list. 
    '''
    f = open(inFile, 'r')
    data = list(map(int, f.read().split()))
    return data

def testFile(inFilename, outFilename):
    '''
    Passes inFilename to readData() to obtain a list of data
    Creates/Resets the output file. 
    Passes the list and the name of output file into testData().
    '''
    print(f"Input File = {inFilename} , Output File = {outFilename}")
    
    # This resets the output file to a blank file. 
    open(outFilename, 'w').close()
    
    data = readData(inFilename)
    testData("RANDOM ORDER", data, outFilename)
    
    data.sort()
    testData("ASCENDING ORDER", data, outFilename)
    
    data.sort(reverse=True)
    testData("DESCENDING ORDER", data, outFilename)
    
        
if __name__ == "__main__":

    main()