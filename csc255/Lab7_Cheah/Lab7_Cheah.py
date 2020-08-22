'''
Ricky Cheah
Lab 7
Main Driver File
'''
from utilities import compareFiles
from rsacodec import RSACodec

def main():
    for i in range(1,4):
        try:
            testFile(i)
        except RuntimeError as err:
            print(err.args[0])

def fileSize(fileObject):
    '''
    Takes in a @fileObject and returns the size of the file. 
    '''
    # This moves the file cursor to the first (0) position, starting from the end (2)
    fileObject.seek(0,2) 
    size = fileObject.tell() # this gets the index of the cursor
    fileObject.seek(0) # this resets the cursor to the beginning
    return(size)

def testEncrypting(rsaCodec, plainFile, encryptedFile, debugObject):
    '''
    Opens the @plainFile and @encryptedFile and passes those to @rsaCodec for
    reading and writing.
    '''
    try:
        f_plainFile = open(plainFile, 'rb')
    except:
        raise RuntimeError(f"Could not open {plainFile} for reading.")
    try:
        # the newline parameter prevents windows from changing \n to \r
        f_encryptedFile = open(encryptedFile, 'w', newline='\n')
        #https://stackoverflow.com/questions/47384652/python-write-replaces-n-with-r-n-in-windows
    
    except:
        raise RuntimeError(f"Could not open {encryptedFile} for writing.")

    debugObject.write(f"\n*** Encrypting {plainFile}, size {fileSize(f_plainFile)} -> {encryptedFile} ***\n\n")
    rsaCodec.encryptStream(f_plainFile, f_encryptedFile, debugObject)
    debugObject.write(f"Encrypted file {encryptedFile} size is {fileSize(f_encryptedFile)}\n\n")
    
    f_plainFile.close()
    f_encryptedFile.close()
    
def testDecrypting(rsaCodec, encryptedFile, decryptedFile, debugObject):
    '''
    Opens the @encryptedFile and @decryptedFile and passes those to @rsaCodec for
    reading and writing.
    '''
    try:
        f_encrypted = open(encryptedFile, 'r')
    except:
        raise RuntimeError(f"Could not open {encryptedFile} for reading.")
    try:
        f_decrypted = open(decryptedFile, 'wb')  
    except:
        raise RuntimeError(f"Could not open {decryptedFile} for writing.")
        
    debugObject.write(f"*** Decrypting {encryptedFile}, size {fileSize(f_encrypted)} -> {decryptedFile} ***\n\n")
    rsaCodec.decryptStream(f_encrypted, f_decrypted, debugObject)
    debugObject.write(f"Decrypted file {decryptedFile} size is {fileSize(f_decrypted)}\n\n")

    f_encrypted.close()
    f_decrypted.close()

def testFile(fileNumber):
    '''
    This function uses the fileNumber and creates all the required file names.
    Those file names are passed into all the neccesary functions to complete the
    encrypting and decrypting process. 
    '''
    
    debugFile = f"{fileNumber}_debug.txt"
    keyMaterialFile = f"{fileNumber}_keymat.txt"
    
    plainFile = f"{fileNumber}_in.dat"
    encryptedFile = f"{fileNumber}_encrypted.txt"
    decryptedFile = f"{fileNumber}_decrypted.dat"
    
    print(f"*** Testing input file {plainFile}, debug output file {debugFile}.\n")
    
    debugObject = open(debugFile, 'w')

    # this extracts p, q and e, then creates an RSACodec instance.
    rsaCodec = makeRSACodecFromFile(keyMaterialFile, debugObject) 
    
    testEncrypting(rsaCodec, plainFile, encryptedFile, debugObject)
    testDecrypting(rsaCodec, encryptedFile, decryptedFile, debugObject)
    
    # compares original file and decrypted file to verify consistency. 
    compareFiles(plainFile, decryptedFile)
    
    debugObject.write(f">>> Files {plainFile} and {decryptedFile} are equal.\n")
    debugObject.close()
    print("OK\n")
    
def makeRSACodecFromFile(fileName, debugObject):
    '''
    This function indentifies and returns p, q, and e values in "X_keymat.txt" files.
    creates an RSACodec instance with those values and and returns it. 
    '''
    f = open(fileName, 'r')
    data = f.read().split()
    
    p = None
    q = None
    e = None
    
    for i in range(0, 5, 2):
        if data[i] == 'p':
            p = data[i+1]
        elif data[i] == 'q':
            q = data[i+1]
        elif data[i] == 'e':
            e = data[i+1]
    f.close()

    if not p:
        raise RuntimeError(f"Unable to extract p from {fileName}.")
    elif not q:
        raise RuntimeError(f"Unable to extract q from {fileName}.")
    elif not e:
        raise RuntimeError(f"Unable to extract e from {fileName}.")
        
    return RSACodec(p, q, e, debugObject)

if __name__ == "__main__":
    main()

