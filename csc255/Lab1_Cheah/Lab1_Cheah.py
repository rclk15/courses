"""
Ricky Cheah
6/13/2020

CSC 255 - Lab 1
""" 
def main():
    # This tests in1.txt until in7.txt
    for i in range(1,8):
        print(SumOfK(f'in{i}.txt',f'out{i}.txt'))
        print("_"*55)

def SumOfK(inFileName, outFileName):
    '''
    1. This function accepts a file "inFileName".
    2. Filters out non-digit characters, and inserts the numbers into a list.
    3. First number in the list is popped out to be a "target"
    5. The remaining list is sorted in ascending order using heapSort() at O(nlog(n))
    4. The sorted list is searched in an O(n) fashion using two pointers, to find if 
        any two numbers or the double of a single number sum up to the "target".
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
    
    
    sortedList = heapSort(numberList)
    outputRows += " ".join(map(str, sortedList)) +"\n" # will be written to output file
    g = open(outFileName, 'w')
    for row in outputRows:
        print(row, end='') # printing output
        g.write(row)   
        
    outputRows = "" # reset outputRows 
    foundSolution = False # Keep tracking of if we found solution

    # Initialize the 2 pointers
    pointer1 = 0
    pointer2 = len(sortedList)-1
    
    # Initialize the repeat number catcher
    previousNumber1 = None
    previousNumber2 = None
    
    # Iterate over numbers with pointers looking for sum == target
    while pointer2>pointer1:
        if previousNumber1 == sortedList[pointer1]: #skips repeat number
            pointer1 += 1
            continue # restarts while loop after moving pointer       
        elif previousNumber2 == sortedList[pointer2]: #skips repeat number
            pointer2 -= 1
            continue    
        else:
            if sortedList[pointer1]*2 == target: # found a number x 2 == target
                foundSolution = True
                outputRows += f"{sortedList[pointer1]}+{sortedList[pointer1]}\n"
                previousNumber1 = sortedList[pointer1]
                pointer1 += 1
                continue
            elif sortedList[pointer2]*2 == target: # found a number x 2 == target
                foundSolution = True
                outputRows += f"{sortedList[pointer2]}+{sortedList[pointer2]}\n"
                previousNumber2 = sortedList[pointer2]
                pointer2 -= 1
                continue
            elif sortedList[pointer1] + sortedList[pointer2] > target: # no match
                pointer2 -= 1
                continue
            elif sortedList[pointer1] + sortedList[pointer2] < target: # no match
                pointer1 += 1
                continue
            else: # found sum of two numbers == target
                foundSolution = True
                outputRows += f"{sortedList[pointer1]}+{sortedList[pointer2]}\n"
                pointer2 -= 1
                pointer1 += 1

    if foundSolution:
        outputRows = "Yes\n" + outputRows
    else:
        outputRows = "No\n" + outputRows
    
    # Finish writing to output file.
    for row in outputRows:
        g.write(row)
    g.close()
    print(outputRows)
    
    return f"Heapsort Version SumOfK({inFileName}, {outFileName}) complete."


def maxHeap(array, size, startIndex):
    '''
    array = name of array/list
    size = size of array to max-heapify
    startIndex = Index of array to max-heapify
    
    This function uses recursion to create a Max Heap
    '''

    largestIntIndex = startIndex # the parent node we are investigating
    leftIndex = 2*startIndex + 1 # left child index
    rightIndex = 2*startIndex + 2 # right child index
    
    if size > leftIndex and array[leftIndex] > array[largestIntIndex]:
        largestIntIndex = leftIndex

    if size > rightIndex and array[rightIndex] > array[largestIntIndex]:
        largestIntIndex = rightIndex

    if largestIntIndex != startIndex: # swapping parent node with largest child
        array[largestIntIndex], array[startIndex] = array[startIndex], array[largestIntIndex]
        
        # after swapping, we now check the child that we swapped, as the parent
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
        
    # This 'deletes' the largest number from heap each time and store it in the last index
    for i in range(size-1, 0, -1):
        array[i], array[0] = array[0], array[i] # swaps root (largest) with last leaf
        maxHeap(array, i, 0) # remake the Max Heap
    return array

if __name__ == "__main__":
    main()
