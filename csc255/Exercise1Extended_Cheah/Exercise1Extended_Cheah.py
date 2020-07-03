"""
Ricky Cheah
6/13/2020

CSC 255 - Exercise 1 Extended
""" 
def main():
    # This tests in1.txt until in6.txt
    for i in range(1,7):
        print(SumOfK(f'in{i}.txt',f'out{i}.txt'))
        print("_"*50)

def SumOfK(inFileName, outFileName):
    '''
    1. This function accepts a file "inFileName".
    2. Filters out non-digit characters, and inserts the numbers into a list.
    3. First number in the list is popped out to be a "target"
    5. The remaining list is sorted in ascending order using heapSort() at O(nlog(n))
    4. The sorted list is searched in an O(n**2) fashion to find if 
        any three numbers or the triple of a single number sum up to the "target".
    5. The results are written into a new file "outFileName". 
    
    * Duplicate results are omitted *
    '''
    print(f"Input file = {inFileName}, Output file = {outFileName}.\n")
    f = open(inFileName, 'r')
    fileRows = f.readlines()
    f.close()
    
    outputRows = ""
    for row in fileRows:
        for ch in row.rstrip(): # rstrip() removes \n at the end of a row
            if ch.isalpha(): # isalpha() returns true if a character is an alphabet
                break
        else: # if we did not break out of the inner for loop, this else is executed
            if row.strip(): # this filters out empty rows
                outputRows += row

    numberList = [int(x) for x in outputRows.split()] # converting string to list of int
    try:
        target = numberList.pop(0) # getting the "target"
    except:
        print("There are no numbers in the file.")
        return f"SumOfK({inFileName}, {outFileName}) failed."
    
    
    sortedList = heapSort(numberList) # sort the list
    outputRows += " ".join(map(str, sortedList)) +"\n" # will be written to output file
    g = open(outFileName, 'w')
    for row in outputRows:
        print(row, end='') # printing what was written to output file
        g.write(row)   
        
    outputRows = "" # reset outputRows 
    foundSolution = False # Keep tracking of if we found solution
    lastIndex = len(sortedList)-1 # last index of list
    
    # These are used to skip repeat numbers.
    previousNumber1, previousNumber2, previousNumber3 = None, None, None

    for i in range(0, lastIndex): # This is the index of the first number
        
        if previousNumber1 == sortedList[i]: # skip repeat
            continue
        
        if sortedList[i]*3 == target: # first number * 3 = target
            foundSolution = True
            outputRows += f"{sortedList[i]}+{sortedList[i]}+{sortedList[i]}\n"
            previousNumber1 = sortedList[i] # keeps track of previous first number
            continue
        
        # This portion below doesnt run when i reaches len(sortedList)-2, because we need
        # at least two indices for the two pointers
        if i < lastIndex - 1: # This portion searches the second and third number
            pointer1 = i+1
            pointer2 = lastIndex
            while pointer2>pointer1:
                
                # if current sum is > than target, or if third number is repeated
                if sortedList[i] + sortedList[pointer1] + sortedList[pointer2] > target or sortedList[pointer2] == previousNumber3:
                    previousNumber3 = sortedList[pointer2] 
                    pointer2 -= 1
                    continue
                
                # if current sum is < than target, or if second number is repeated
                elif sortedList[i] + sortedList[pointer1] + sortedList[pointer2] < target or sortedList[pointer1] == previousNumber2:
                    previousNumber2 = sortedList[pointer1]
                    pointer1 += 1
                    continue
                
                # found a valid solution!
                else:
                    foundSolution = True
                    outputRows += f"{sortedList[i]}+{sortedList[pointer1]}+{sortedList[pointer2]}\n"
                    previousNumber3 = sortedList[pointer2]
                    previousNumber2 = sortedList[pointer1]
                    pointer2 -= 1
                    pointer1 += 1
            
            previousNumber1 = sortedList[i] # keeping track of previous first number. 

    if foundSolution:
        outputRows = "Yes\n" + outputRows
    else:
        outputRows = "No\n" + outputRows

    print(outputRows) # printing what was written to output file
    for row in outputRows:
        g.write(row)

    g.close()
    return f"Heapsort Version SumOfK({inFileName}, {outFileName}) complete."

def maxHeap(array, size, startIndex):
    '''
    array = name of array/list
    size = size of array to max-heapify
    startIndex = Index of array to max-heapify
    
    This function uses recursion to create a Max Heap
    '''
    largestIntIndex = startIndex
    leftIndex = 2*startIndex + 1
    rightIndex = 2*startIndex + 2

    if size > leftIndex and array[leftIndex] > array[largestIntIndex]:
        largestIntIndex = leftIndex

    if size > rightIndex and array[rightIndex] > array[largestIntIndex]:
        largestIntIndex = rightIndex

    if largestIntIndex != startIndex:
        array[largestIntIndex], array[startIndex] = array[startIndex], array[largestIntIndex]
        maxHeap(array, size, largestIntIndex)


def heapSort(array):
    '''
    array = name of array to be sorted
    
    Making use of MaxHeap function, this function sorts an array in ascending order.
    O(nlog(n))
    '''
    size = len(array)
    startIndex = size//2 - 1 # this finds start of the non-leaf indexes
    
    # This builds the first Max Heap
    for i in range(startIndex, -1, -1): 
        maxHeap(array, size, i)
        
    # This 'deletes' the largest number from heap and store it in the last index
    for i in range(size-1, 0, -1):
        array[i], array[0] = array[0], array[i] # swaps root (largest) with last leaf
        maxHeap(array, i, 0) # remake the Max Heap
    return array

if __name__ == "__main__":
    main()
