'''
Recursion Extra Credit 
May 02, 2020
Author: Ricky Cheah

Driver program to compare two approaches to a  problem, one recursive, the other iterative.
Problem: Generating a set of combinations of "1"s and "0"s without three consecutive "0"s. 

-May 02 2020: Added toBinary
'''

def noThreeOsStrings(n):
    '''
    Recursive approach. 
    Author: Ricky Cheah
    '''

    def toBinary(number):
        '''
        Function to convert an integer to binary form using recursion. 
        '''
        if number == 0:
            return 0
        else:
            return (number % 2 + 10 * (toBinary(int(number / 2))))

    def generateStrings(n1, n2):
        '''
        n1 and n2 are integers.
        Recursive function to return all values between n1 and n2(inclusive) 
        in string binary form without 3 consecutive 0s.
        '''
        if n1 == 0:
            return ['0']
        elif n1 > n2-1:
            newNumber = str(toBinary(n1))
            if check3Zero(newNumber, 0):
                return [newNumber] + generateStrings(n1-1, n2)
            else:
                return generateStrings(n1-1, n2)
        else:
            return []
    
    def addZero(list1):
        '''
        Takes a list and adds a '0' in front of every element.
        Does not return elements with 3 consecutive 0s. 
        '''

        if list1: 
            nextList = list1[1:]
            newNumber = '0' + list1[0]
            if check3Zero(newNumber,0):
                return [newNumber] + addZero(nextList) #bug note: append() returns None. 
            else:
                return addZero(nextList)
        else:
            return []
    
    
    def check3Zero(number, count = 0):
        '''
        Takes a number and returns False if it contains 3 consecutive 0s.
        Returns True otherwise.
        count keeps track of how many consecutive 0s are contained. 
        '''

        if count == 3:
            return False
        elif number == '':
            return True
        else:
            if number[0] == "0":
                count += 1
            else: 
                count = 0
            return check3Zero(number[1:], count)

    #Base Case
    if n == 0: 
        return {"0"}
    
    #Recursive Case
    else:
        return set(generateStrings((2**n)-1,2**(n-1))) | set(addZero(list(noThreeOsStrings(n-1))))


    
def noThreeOsStringsAnswer(length):
    '''
    Iterative approach.
    Code copied from question specifications. 
    Author: Ivan Temesvari
    '''
    if length == 0:
        return ['']
    s = [ "0", "1" ]
    o = []
    count = 1
    while count < length:
        for item in s:
            p = str(item) + "0"
            if not "000" in p:
                o.append(str(item) + "0")
            o.append(str(item) + "1")
        s = o
        o = []
        count += 1
    return set(s)

    
def main():
    '''
    Compares the returned sets by the two approaches.
    '''
    
    n = 3
    
    print("Recursion Set\n",noThreeOsStrings(n))
    print("Iterative Answer Set (from specification)\n",noThreeOsStringsAnswer(n))
   
    print(f"\nAre the two sets the same for n = {n} -",noThreeOsStrings(n) == noThreeOsStringsAnswer(n))
    n = 4
    print(f"\nAre the two sets the same for n = {n} -",noThreeOsStrings(n) == noThreeOsStringsAnswer(n))
    n = 6
    print(f"\nAre the two sets the same for n = {n} -",noThreeOsStrings(n) == noThreeOsStringsAnswer(n))    
    n = 8
    print(f"\nAre the two sets the same for n = {n} -",noThreeOsStrings(n) == noThreeOsStringsAnswer(n))

if __name__ == '__main__':
    main()
    
