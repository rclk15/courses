"""
Ricky Cheah
6/26/2020
Exercise 3 
"""
import random

def main():
    generateNumbers(100, 1, 10000, 'out1.txt')
    generateNumbers(100, 1, 10000, 'out2.txt', False)
    generateNumbers(100, 1, 10000, 'out3.txt', True)
    
def generateNumbers(totalNumbers: int, lowerRange: int, upperRange:int, \
                    outFile: str, sort: bool = None):
    '''
    A list numbers (totalNumbers) will be generated from a lower range and upper range, and 
    could be sorted based on 'sort' input.
    if sort is False, data will be sorted in ascending order.
    if sort is True, data will be sorted in descending order.
    
    '''
    print(f"Generating {totalNumbers} numbers from range ({lowerRange},{upperRange}).")
    print(f"Output file is: {outFile}\n")
    
    seed = 2020 # this is used to make random output the same every time.
    random.seed(seed) # setting the seed
    
    finalList = []
    for count in range(totalNumbers):
        finalList.append(random.randint(lowerRange, upperRange))

    # sorting portion
    if sort != None:    
        finalList.sort(reverse = sort)
    f = open(outFile, 'w')
    
    # writes to output file
    for item in finalList: 
        f.write(str(item) + "\n")

    f.close() 

if __name__ == "__main__":
   main() 
    
    


