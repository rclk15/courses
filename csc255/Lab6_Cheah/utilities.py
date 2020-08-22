'''
Ricky Cheah
Lab 6
7/17/2020

Various assistive functions. 
'''

def bytePresentation(byte):
    '''
    This function takes in a byte, and returns the printable string form of the byte.
    Aids in writing to output files. 
    '''
    if byte == b'\n': return "\\n"
    if byte == b'\r': return "\\r"
    if byte == b'\t': return "\\t"
    
    if byte >= b' ' and byte <= b'~':
        return str(f"'{byte.decode('utf-8')}'")
    else:
        return f"0x{byte.hex()}"