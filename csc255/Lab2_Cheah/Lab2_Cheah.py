"""
Ricky Cheah
6/19/2020
Lab 2 

The strings can be encoded with 5 digits instead of 6, 
using a Base 27 number system. See encode().
"""

def main():
    for i in [10, 100]:
        stringSorting(f"in_abc{i}.txt", f"out_abc{i}.txt")


def encode(string, maxCharacter):
    '''
    This function encodes the string provided with integers.
    maxCharacter is the maximum number of characters that is possible with string.
    maxCharacter must be set properly for 'aa' to come before 'b', for example. 
    
    It takes the lower case of each alphabet and converts it to an integer first:
        a = 1, b = 2, ... z = 26
    Then it converts the numbers corresponding to the string
    into a Base 27 number system.
    For example, azc:
    a z c = 01 26 03
    the final number can be calculated by:
    (1*27**2) + (26*27**1) + (3*27**0) = 1434
    '''
    encoded = 0
    
    for ch in string:
        encoded = encoded*27 + (ord(ch) - 96)
        maxCharacter -= 1
        
    # this section makes sure alphabetical orders are kept.
    # for example, "azz" should come before "b"
    while maxCharacter > 0:
        encoded = encoded*27
        maxCharacter -= 1
    return encoded

def stringSorting(inFilename, outFilename):    
    '''
    This function takes inFilename and "processes" the data in the file,
    creating a list tuples of the strings and their encoded numbers to be sorted.
    This list is then used when calling countSort and bubbleSort to sort the list.
    The return values of those two functions are written into outFilename.
    
    Note: The maxCharacter parameter for encode() must be set to the maximum
    number of characters each string can contain to maintain proper alphabetical sorting.
    We must know this maxCharacter before we begin encoding, otherwise we would need
    another for loop to find it. 
    '''
    f = open(inFilename, 'r')
    data = f.read()
    f.close()
    dataLen = len(data)
    stringList = []

    # This portion skips non relevant strings. 
    i = 0
    try:
        while data[i] != "=": # skips everything before =
            i += 1
        i+=1
    except:
        print("The input file is empty! \nPlease provide 'maxValue = (max string here)'")
        print("Program terminated.")
        return

    # This portion collects the strings into stringList to be processed
    # This string is encoded first, and the encoded value and the string is 
    # passed into stringList as a tuple. This uses more space but saves us time
    # because we don't have to encode the string again.
    # The stringList will look like: [(729, 'a'), (1836, 'bn'), (16998, 'who')]
    tempString= str()  
    while i < dataLen:
        if data[i].isalpha():
            tempString = tempString + data[i].lower()
            if i == dataLen - 1: # this makes sure we don't miss the last number
                stringList.append((encode(tempString, 3),tempString))
        else:
            if tempString: # catch initial whitespace
                stringList.append((encode(tempString, 3),tempString)) 
                tempString= str() 
        i += 1
    
    countSorted = countingSort(stringList)
    bubbleSorted = bubbleSort(stringList)

    if not countSorted or not bubbleSorted: # No elements provided. 
        print("Program terminated.")
        return
    
    if countSorted == bubbleSorted:
        print("Both Count Sort and Bubble Sort produced the same results.")
    
    outFilaA = outFilename.replace(".", "a.")
    g = open(outFilaA, 'w')
    g.write(' '.join(map(str,countSorted)))
    g.close()
    print(f"Count Sort Output File = {outFilaA}")
    
    outFilaB = outFilename.replace(".", "b.")
    h = open(outFilaB, 'w')
    h.write(' '.join(map(str,bubbleSorted)))
    h.close()
    print(f"Bubble Sort Output File = {outFilaB}\n")
    
    return "Sorting and Writing to file completed"
    
def countingSort(array):
    '''
    This function takes in an array/list filled with tuples and sorts 
    them using Count Sort, according to the tuple's first element.
    The first element is the encoded number of the string (the second element)
    Returns the sorted array. 
    The stringList looks like: [(729, 'a'), (1836, 'bn'), (16998, 'who')]
    '''
    stringList = array[:] # localized version, so that original array not changed. 
    try:
        maxNumber = stringList.pop(0)[0] # this is the provided max
    except:
        print("Please provide a maxValue!")
        return
    if not stringList:
        print("Please provide strings to be sorted!")
        return


    maxIndex = 1
    for i in range(2, len(stringList)):
        if stringList[i][0] > stringList[maxIndex][0]:
            maxIndex = i
    # confirm that the max we found is smaller than the provided
    if stringList[maxIndex][0] <= maxNumber:
        maxNumber = stringList[maxIndex][0]
    else:
        print("Error! Provided maxValue surpassed by elements to be sorted!")
        return
    countList = [0]*(maxNumber+1) # need + 1 to include the actual last number
    
    # This populates the count list with number of occurence of each string
    for i in range(len(stringList)):
        countList[stringList[i][0]] += 1
        
    # This updates the count list to have the starting index of each string in sorted list.
    for i in range(1, len(countList)):
        countList[i] += countList[i-1]
    
    # This populates the final sortedList, ignoring the encoding. 
    sortedList = [0]*len(stringList)
    for i in range(len(stringList)-1, -1, -1):

        sortedList[countList[stringList[i][0]]-1] = stringList[i][1]
        countList[stringList[i][0]] -= 1
    return sortedList
    
def bubbleSort(array):
    '''
    This function takes in an array/list of tuples and sorts it using Bubble Sort,
    according to the tuples' first elements.
    Returns the sorted array with the tuples' second elements only. 
    '''
    localArray = array[1:] # skip first number (k)
    for i in range(len(localArray)-1):
        for j in range(0, len(localArray)-i-1):
            if localArray[j][0] > localArray[j+1][0]:
                localArray[j], localArray[j+1] = localArray[j+1], localArray[j]
                
    # This returns the array with the strings only, eliminating the encoding
    for i in range(len(localArray)):
        localArray[i] = localArray[i][1]
    
    return localArray

if __name__ == "__main__":
    main()