"""
Ricky Cheah
6/13/2020

CSC 255 - Exercise 1
""" 
def main():
    # This tests in1.txt until in5.txt
    for i in range(1,6):
        print(SumOfK(f'in{i}.txt',f'out{i}.txt'))
        print("_"*50)
    

def SumOfK(inFileName, outFileName):
    '''
    1. This function accepts a file "inFileName".
    2. Filters out non-digit characters, and inserts the numbers into a list.
    3. First number in the list is popped out to be a "target"
    4. The search rest of the numbers in the list in an O(n**2) fashion to find if 
        any two numbers or the double of a single number sum up to the "target".
    5. The results are written into a new file "outFileName". 
    '''
    print(f"Input file = {inFileName}, Output file = {outFileName}.\n")
    f = open(inFileName, 'r')
    fileRows = f.readlines()
    f.close()
    
    # This portion filters out the non-digit characters
    outputRows = ""
    for row in fileRows:
        for ch in row.rstrip(): # rstrip() removes \n at the end of a row
            if ch.isalpha(): # isalpha() returns true if a character is an alphabet
                break 
        else: # if we did not break out of the inner for loop, these are executed
            if row.strip(): # this filters out empty rows
                outputRows += row
    
    # This writes them into the output file        
    g = open(outFileName, 'w')
    for row in outputRows:
        g.write(row)
        print(row, end='') # This prints out what was written to output file.
    
    # This converts those numbers into a list
    numberList = [int(x) for x in outputRows.split()]
    try:
        target = numberList.pop(0) # getting the "target"
    except:
        print("There are no numbers in the file!")
        return f"SumOfK({inFileName}, {outFileName}) failed."
    
    outputRows = ""
    
    foundSolution = False # keep track of if we found solution
    
    for i in range(len(numberList)):           
        if numberList[i]*2 == target: # number*2 == target
            foundSolution = True
            outputRows += f"{numberList[i]}+{numberList[i]}={target}\n"
        else:
            for j in range(i+1, len(numberList)):
                if numberList[i] + numberList[j] == target: # number1 + number2 == target
                    foundSolution = True
                    outputRows += f"{numberList[i]}+{numberList[j]}={target}\n"
    if foundSolution:
        outputRows = "Yes\n" + outputRows
    else:
        outputRows = "No\n" + outputRows
    
    # Finalize writing to output file. 
    for row in outputRows:
        g.write(row)
    g.close()
    
    print(outputRows) # This prints out what was written to output file.
    
    return f"SumOfK({inFileName}, {outFileName}) complete."

if __name__ == "__main__":
    main()
