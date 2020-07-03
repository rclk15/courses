"""
Ricky Cheah
6/19/2020
Exercise 2 

Since the complexity of Count Sort is O(n + k), where
k is the max range of our numbers, if k is a large number, 
for example, k >= n**2, then the complexity becomes O(n + n**2),
which is O(n**2). In that case, Merge Sort will be better.
"""

def main():
    
    # This tests both in10.txt and in100.txt  
    for i in [10, 100]:
        numberSorting(f"in{i}.txt", f"out{i}.txt")


def numberSorting(inFilename, outFilename):
    '''
    This function takes inFilename and "processes" the data in the file,
    creating a list of numbers to be sorted.
    This list is then used when calling countSort and bubbleSort to sort the list.
    The return values of those two functions are written into outFilename.
    '''
    print(f"Input file = {inFilename}")
    f = open(inFilename, 'r')
    data = f.read()
    f.close()
    dataLen = len(data)
    numberList = []
    
    tempNumber = int() 
    for i in range(dataLen):
        if data[i].isdigit():
            tempNumber = tempNumber*10 + int(data[i])
            if i == dataLen - 1: # this makes sure we don't miss the last number 
                numberList.append(tempNumber)
        else:
            if data[i-1].isdigit(): # this makes sure tempNumber indeed has a number
                numberList.append(tempNumber)
                tempNumber = int()
    
    # Sorting
    countSorted = countSort(numberList)
    bubbleSorted = bubbleSort(numberList)
    
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

                
def bubbleSort(array):
    '''
    This function takes in an array/list and sorts its elements using Bubble Sort.
    Returns the sorted array. 
    '''
    localArray = array[1:] # make a local copy, ignoring the first element (k)
    for i in range(len(localArray)-1):
        for j in range(0, len(localArray)-i-1):
            if localArray[j] > localArray[j+1]:
                localArray[j], localArray[j+1] = localArray[j+1], localArray[j]
    return localArray

def countSort(array):
    '''
    This function takes in an array/list and sorts its elements using Count Sort.
    Returns the sorted array. 
    '''
    numberList = array[:] # make a local copy
    try:
        k = numberList.pop(0) # getting k (the given largest element)
    except:
        print("There are no numbers in input file!")
        return
    if not numberList:
        print("There are no elements to sort in input file!")
        return
        

    # This portion determines actual k (the max value) and compares it to the provided k
    maxIndex = 1
    for i in range(2, len(numberList)):
        if numberList[i] > numberList[maxIndex]: 
            maxIndex = i
    if numberList[maxIndex] <= k: # largest value found is less than given k, OK.
        k = numberList[maxIndex] 
    else:
        print("Error! Provided k surpassed by elements to be sorted!")
        return
    # After this is completed, we have the actual largest k value in the list.
    
    countList = [0]*(k+1)  # need + 1 to include the actual last number

    # This populates the count list with the respective element counts
    for i in range(len(numberList)):
        countList[numberList[i]] += 1
    
    # This modifies the count list with the index where each element starts
    for i in range(1, len(countList)):
        countList[i] += countList[i-1]

    # This creates and populates a sorted list that will be returned
    sortedList = [0]*len(numberList)
    for i in range(len(numberList)-1, -1, -1):
        sortedList[countList[numberList[i]]-1] = numberList[i]
        countList[numberList[i]] -= 1
    
    return sortedList

if __name__ == "__main__":
    main()