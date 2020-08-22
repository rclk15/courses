'''
Ricky Cheah
Lab 7
RSAAlgorithm Class
'''
class RSAAlgorithm(object):
    '''
    This class stores all the RSA parameters and performs the encryption and decryption. 
    '''
    def __init__(self, p, q, e, debugObject):
        '''
        calculates all the necessary RSA parameters. 
        '''
        self._debugObject = debugObject
        self._p = p
        self._q = q
        self._e = e
        
        self._n = self._p*self._q
        self.phi_n = (self._p-1)*(self._q-1)
        self._d = gcdExtended(self._e, self.phi_n, 0)
        self.debugPrint()
        
    def debugPrint(self):
        '''
        prints the out the RSA parameters to debugObject.
        '''
        self._debugObject.write("--- RSAAlgorithm\n")
        self._debugObject.write(f"p {self._p}\n")
        self._debugObject.write(f"q {self._q}\n")
        self._debugObject.write(f"e {self._e}\n")
        self._debugObject.write(f"n {self._n}\n")
        self._debugObject.write(f"d {self._d}\n")
        
    def encrypt(self, bigNumber):
        '''
        encryptes the number.
        note: (bigNumber**self._e) % self._n <<< this crashes python. 
        '''
        encryptedNumber = pow(bigNumber, self._e, self._n)
        self._debugObject.write(f"RSAAlgorithm::encrypt {hex(bigNumber).upper()}" +
                                f" -> {hex(encryptedNumber).upper()}\n\n")
        return encryptedNumber
        
    def decrypt(self, bigNumber):
        '''
        decryptes the number. 
        '''
        decryptedNumber16 = hex(pow(bigNumber, self._d, self._n))
        
        self._debugObject.write(f"RSAAlgorithm::decrypt {hex(bigNumber).upper()}" +
                                f" -> {decryptedNumber16.upper()}\n\n")
        return decryptedNumber16
    
def gcdExtended(a, b, recursionLevel):  
    '''
    This is the extended euclidian algorithm used to find inverse modulo. 
    '''
    if a == 0 :  
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b%a, a, recursionLevel+1) 
    x = y1 - (b//a) * x1  
    y = x1  
    if recursionLevel: # if recursionLevel not 0, we are not at the first level, so we keep keep recursion going.
        return gcd, x, y 
    else: # the highest level so return x. Make sure x is positive by %
        return x%b 