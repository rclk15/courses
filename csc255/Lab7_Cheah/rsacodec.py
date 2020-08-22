'''
Ricky Cheah
Lab 7
RSACodec Class
'''
from rsaalgorithm import RSAAlgorithm
from utilities import BlockReader, BlockWriter

class RSACodec(object):
    '''
    This class serves as a wrapper around RSAAlgorithm class.
    Receives the necessary file names from the driver file and passes file objects
    to the appropriate RSAAlgorithm methods for encrypting and decrypting. 
    '''
    def __init__(self, p, q, e, debugObject):
        self._p = int(p)
        self._q = int(q)
        self._e = int(e)
        # creates a RSAAlgorithm instance with the correct public and private keys for use
        self.rsaAlgorithm = RSAAlgorithm(self._p, self._q, self._e, debugObject)

    def maxBlockLength(self):
        '''
        n is calculated using p and q, then the maximum allowable bytes that can 
        be read per block is calculated.
        0xFF..FF has to be < n. 
        ** we device by two because 0xFF is 1111 in bits(binary), 
        so one byte can contain 0xFFFF
        '''
        n = self._p*self._q
        hex_n = hex(n)[2:] # converting n to hex, but this is in str.
        length_n = len(hex_n) 
        maxBlock = int(((length_n - length_n % 2) / 2) - 1) # **
        if maxBlock < 1:
            raise RuntimeError(f"maxBlockLength - Modulus {maxBlock} is too small.")
        return maxBlock
    
    def encryptStream(self, f_plainFile, f_encryptedFile, debugObject):
        '''
        Receives the necessary file objects and calls the appropriate methods to
        encrypt the data and writes to file. 
        '''
        blockMaxLength = self.maxBlockLength()
        blockReader = BlockReader(f_plainFile, blockMaxLength, debugObject)
        
        dataRemains = True # updates every loop
        loopCount = 0
        while dataRemains:
            debugObject.write(f"--- RSACodec::encryptStream block #{loopCount}, max length {blockMaxLength} ---\n\n")
            data = blockReader.readData() # returned in tuple form 
            bigNumber = data[0]
            width = data[1]
            
            cipherNumber = self.rsaAlgorithm.encrypt(bigNumber)
            
            f_encryptedFile.write(f"{hex(width)[2:].upper()} {hex(cipherNumber)[2:].upper()}\n")

            dataRemains = blockReader.dataRemains()
            loopCount += 1

    def decryptStream(self, f_encrypted, f_decrypted, debugObject):
        '''
        Receives the necessary file objects and calls the appropriate methods to
        decrypt the data and writes to file. 
        '''     
        blockWriter = BlockWriter(f_decrypted, debugObject)
        loopCount = 0
        dataLine = f_encrypted.readline().split()
        while dataLine:
            # this is just the way the data is stored in the encrypted file.
            blockLength = int("0x" + dataLine[0], 16) # This adds 0x to the str, then converts it to int (base 16 hex). 
            cipherNumber = int("0x" + dataLine[1], 16)
            
            debugObject.write(f"--- RSACodec::decryptStream block #{loopCount}, length {blockLength} ---\n\n")
            decryptedNumber16 = self.rsaAlgorithm.decrypt(cipherNumber)

            decrypt_int = int(decryptedNumber16[2:],16) # converting a hex string into decimals
            
            blockWriter.writeData(decrypt_int, blockLength)
            
            dataLine = f_encrypted.readline().split()
            loopCount += 1

