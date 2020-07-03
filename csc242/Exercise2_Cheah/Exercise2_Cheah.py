'''
Ricky Cheah
2/12/2018

Driver Program to compare 3 different methods of computing fibonacci number.
1.Modified recursive Fibonacci function to employ memoization
2.Original recursive technique (code by Ken Lambert).
3.Iterative technique (code by Ken Lambert).

The timing of method 1 and 3 are similar; they have a linear runtime of O(n)
The timing of method 2 is exponential; it has a runtime of form O(k^n).
    If we solve for k, k will turn out to be the golden ratio, 1.61
'''

from counter import Counter
import time

def fib(n, counter, dictionary = {}):
    """Count the number of recursive calls of the Fibonacci
    function with memoization."""
    counter.increment() 
    if n in dictionary: #check if we already computed this value
        return dictionary[n]
    elif n < 3: #base case
        dictionary[n] = 1
        return dictionary[n]
    else: #recursion here
        dictionary[n-2] = fib(n-2, counter, dictionary)
        dictionary[n-1] = fib(n-1, counter, dictionary)
        dictionary[n] = dictionary[n-1] + dictionary[n-2]
        return dictionary[n]


def fibRecursive(n, counter):
    """Count the number of recursive calls of the Fibonacci
    function.
    Author: Ken Lambert
    """
    counter.increment()
    if n < 3:
        return 1
    else:
        #recursion here
        return fibRecursive(n - 1, counter) + fibRecursive(n - 2, counter)


def fibLoop(n, counter):
    """Count the number of iterations in the Fibonacci
    function.
    Author: Ken Lambert
    """
    sum = 1
    first = 1
    second = 1
    count = 3
    while count <= n:
        counter.increment()
        sum = first + second
        first = second
        second = sum
        count += 1
    return sum


header = ("Size", "Calls", "Fibonacci", "Time")
spacing = (20, 10, 60, 15) #spacings for the different columns
print(f"{header[0]:>{spacing[0]}} {header[1]:>{spacing[1]}} {header[2]:>{spacing[2]}} {header[3]:>{spacing[3]}}")
print("\nMemoization\n")

problemSize = 2
for count in range(8):
    counter = Counter()

    # The start of the algorithm
    startTime = time.time()
    answer = fib(problemSize, counter)
    endTime = time.time()
    totalTime = round(endTime - startTime, spacing[3]-5)
    # The end of the algorithm

    print(f"{problemSize:>{spacing[0]}} {str(counter):>{spacing[1]}} {answer:>{spacing[2]}} {totalTime:>{spacing[3]}}")
    problemSize *= 2
    
print("\nRecursive\n")

problemSize = 2
for count in range(5):
    counter = Counter()

    # The start of the algorithm
    startTime = time.time()
    answer = fibRecursive(problemSize, counter)
    endTime = time.time()
    totalTime = round(endTime - startTime, spacing[3]-5)
    print(f"{problemSize:>{spacing[0]}} {str(counter):>{spacing[1]}} {answer:>{spacing[2]}} {totalTime:>{spacing[3]}}")
    problemSize *= 2
    
print("\nIteration\n")

problemSize = 2
for count in range(8):
    counter = Counter()

    # The start of the algorithm
    startTime = time.time()
    answer = fibLoop(problemSize, counter)
    endTime = time.time()
    totalTime = round(endTime - startTime, spacing[3]-5)
    print(f"{problemSize:>{spacing[0]}} {str(counter):>{spacing[1]}} {answer:>{spacing[2]}} {totalTime:>{spacing[3]}}")
    problemSize *= 2
    
    
    