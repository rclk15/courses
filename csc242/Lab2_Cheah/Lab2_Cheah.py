'''
Ricky Cheah
Feb 14, 2020

This program modifies the quicksort function so that it calls insertionsort 
to sort any sublist whose size is less than a specific threshold of items. 

A table with rows of different threshold number and columns of different list
sizes is generated to show their relationship. 

All quicksort and insertionsort codes are orignally by Ken Lambert.
'''


from profiler import Profiler
import random #to generate numbers in list

def insertionSort(lyst, left, right, profiler):
    '''
    Code for insertion sort.
    Takes in an entire list (lyst), 
        but only sorts items between "left" and "right" index. 
    profiler object helps to keep a count of different operations and time. 
    '''
    i = left + 1
    while i < right + 1:
        exchanged = False #to keep better count of exchanges
        itemToInsert = lyst[i]
        j = i - 1
        while j >= 0: 
            profiler.comparison()
            if itemToInsert < lyst[j]:
                lyst[j + 1] = lyst[j]
                profiler.exchange()
                j -= 1
                exchanged = True
            else:
                break
        lyst[j + 1] = itemToInsert
        if exchanged:
            profiler.exchange() #only increase if we actually did exchange
        i += 1

def quicksort(lyst, mod, threshold, profiler):
    '''
    The main quicksort program, takes in the initial full list (lyst) for sorting.
    Calls the quicksortHelper function to start sorting. 
    mod: if True, runs quicksort below a certain list length.
    threshold: list length to use quicksort. 
    '''
    quicksortHelper(lyst, 0, len(lyst) - 1, mod, threshold, profiler)

def quicksortHelper(lyst, left, right, mod, threshold, profiler):
    '''
    Passes the list to the partition function, and split using pivotLocation. 
    left: start index of partial list
    right: end index of partial list.
    mod: if True, runs quicksort below a certain list length.
    threshold: list length to use quicksort. 
    '''
    if left < right:
        if mod and right - left < threshold: #check if need to use insertionsort
            insertionSort(lyst, left, right, profiler)
            
        else: #continue with quicksort
            pivotLocation = partition(lyst, left, right, profiler)
            quicksortHelper(lyst, left, pivotLocation - 1, mod, threshold, profiler)
            quicksortHelper(lyst, pivotLocation + 1, right, mod, threshold, profiler)

def partition(lyst, left, right, profiler):
    '''
    Takes in a list partially sorts between "left" and "right" index. 
    Determines the pivot, and moves items smaller than pivot to the left side.
    Returns the boundary location for further splitting. 
    '''
    # Find the pivot and exchange it with the last item
    middle = (left + right) // 2
    profiler.exchange()
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    # Set boundary point to first position
    boundary = left
    # Move items less than pivot to the left, move boundary if swapped
    for index in range(left, right):
        profiler.comparison()
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            profiler.exchange()
            boundary += 1
    # Exchange the pivot item and the boundary item
    swap (lyst, right, boundary)
    profiler.exchange()
    return boundary

def swap(lyst, i, j):
    """
    Exchanges the items at positions i and j.
    """
    # You could say lyst[i], lyst[j] = lyst[j], lyst[i]
    # but the following code shows what is really going on
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp


def main():
    '''
    Shows the time difference and numbers of comparisons & exchanges 
    for original quicksort and modified quicksort 
    '''
    p = Profiler()
    #this sample list is taken from Lab2's example
    lyst1 = [18, 9, 31, 23, 8, 34, 43, 34, 33, 33, 17, 19, 51, 14, 3, 16, 31, 21, 48, 44, 29, 24, 13, 26, 31, 18, 37, 11, 48, 27, 26, 38, 7, 40, 24, 45, 29, 11, 46, 48, 8, 21, 15, 43, 7, 42, 47, 17, 44, 51]
    #the list is copied to ensure the test results are comparable. 
    lyst2 = lyst1[:]


# UNCOMMENT print statements to view lists before and after sorting.
#    print(lyst1, "\n")
    print(p.test(quicksort, lyst1, comp = True, exch = True, mod = False))
#    print("Sorted:\n", lyst1, "\n")
    
#    print(lyst2, "\n")
    print(p.test(quicksort, lyst2, comp = True, exch = True, threshold = 10, mod = True))
#    print("Sorted:\n", lyst2, "\n")

    print("After sorting, List 1 == List 2:", lyst1 == lyst2)
    print("_"*80)
    
    #this portion generates a list with randomized numbers
    size = 5000
    lyst = []
    for count in range(size):
        lyst.append(random.randint(1, size + 1))
    lyst1 = lyst[:]
    lyst2 = lyst[:]
    print(p.test(quicksort, lyst1, comp = True, exch = True, mod = False))
    print(p.test(quicksort, lyst2, comp = True, exch = True, threshold = 10, mod = True))
    
    print("After sorting, List 1 == List 2:", lyst1 == lyst2)
    print("_"*80)
    findBestCase()

def findBestCase():
    '''
    Function to compile a table of the time used for sorting for:
        different list sizes and threshold values.
    '''
    p = Profiler()
    masterList = [] #list to contain the lists of different sizes
    resultNoMod = []
    
    print(" "*2, end = "")
    for exponent in range(1,5): #this creates the master list using random numbers for different list sizes
        size = 5*10**exponent
        
        lyst = []
        for count in range(size):
            lyst.append(random.randint(1, size + 1))
        masterList.append(lyst)
        print(f"{size:<13}", end = "") #this prints the table headers (list size)
    print()
    
    #this creates the results for non-modified quicksort
    for i in range(0, len(masterList)): 
        tempLyst = masterList[i][:] #create list so we don't change the master list
        resultNoMod.append(repr(p.test(quicksort, tempLyst, mod = False)))
    print(resultNoMod, "Not Modified")
    

    #this creates the results for non-modified quicksort, with different thresholds
    for multiplier in range (1,5):
        resultMod = []
        thresholdValue = multiplier * 10
        for i in range(0, len(masterList)): 
            tempLyst = masterList[i][:] #create list so we don't change the master list
            resultMod.append(repr(p.test(quicksort, tempLyst, threshold = thresholdValue, mod = True)))
        print(resultMod, "Threshold =", thresholdValue) #prints threshold
        
if __name__ == "__main__":
    main() 


'''
1. The performance of modified quicksort is very dependent on the threshold:
    from the graph generated we see that a threshold of around 10 is optimum. 
    
2. The size of the list doesn't affect the modification; it performs better
    than the original quicksort each time (when threshold is 10).
    This improvement is noticeable with larger list sizes (>5000).
    
3. Insertionsort should be used instead of quicksort when the list 
    is "small enough", around 10 items as seen from the table. 
    
4. The difference is small; the modified version performs a little
     more comparions, but a little less exchanges. 

    For example, in a random list of 5000 items, the modified 
    quicksort did around 75000 comparisons and 41000 exchanges, 
    compared to the original versions 74000 and 41600. 
    
'''