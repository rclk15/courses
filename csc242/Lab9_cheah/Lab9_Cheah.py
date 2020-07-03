"""
Ricky Cheah
Lab 9
4/17/2020

Added functions in hashset.py:
cellLoadFactor() returns the number of occupied array cells divided 
by the array's capacity. 
printChains() displays the array cells with their chains. 
_______________________________________________________________________________
1. The insertion performance between inserting the integers in order and inserting 
the integers randomly not the same. 

--Capacity 100--
Each insertion is O(1) when we insert in order.
Rehashing is O(n), so the time taken to insert 1-400 to a HashSet of 100 initial
capacity will be longer than that of Capacity 500 because of trigerring rehash() thrice.

With random insertion, insertion is O(1) in the best case, O(n) in the worse case if 
we are inserting into an index that is growing without bounds. This is due to our add() 
only checks for cellLoadFactor() > 0.80, and not loadFactor().  

--Capacity 500--
In the case of integers from 1 to 400, there are 400 total integers to insert. 
In both the random and in-order implementation, the add() method in HashSet 
will have to go through all 400 integers eventually, and it takes the same amount
of time for each integer to be added in both implementations. No rehash() needed.
In other words, both implementations will go through the same 400 add() methods, 
and each of those add() methods will have the same random access O(1) performance.  

Additional info on test design: 
1. We only count the time used to add the integers (this includes rehash()).
2. In the random implementation, we don't attempt to add an already added 
integer into the HashSet to be consistent. Otherwise, lots of wasted time 
will wasted in __contains__.

2. The search performance for 3 in both cases will be same.
This is the case because our modified add() function calls rehash() automatically
when cellLoadFactor() returns a value of > 0.80.
This is also due to the fact that we are adding 1 to 80 sequentially using 
a straightforward hash() method which will add the items to the array from the 0 
index to the last index, and and circles back to the 0 index, without any 
index having chains.

If we are not adding sequentially, say if we add 3, 103, 203, 303.. All these items 
will reside in index 3, and rehash() won't be triggered, and we will have longer 
search times when we search for 3, because 3 will be at the back of the chain. 

This shows that might be a good idea to instead of just checking cellLoadFactor(), 
an additional check should be performed each time a chain is increased in length
so that we could consider to rehash() when a chain is over a certain length.
In the case of 3, 103, 203, 303 in a chain, when we rehash(), the chain of index 3
will decrease in half because 103 and 303 will reside position index 103. 

3. The search performance for 3 in both cases will be the same because we have random 
access performance O(1), with rehash() ensuring no chains.

As an aside, with a 100 capacity, if we add 1 - 303 and don't rehash(), 
then at index 3, the chain will look like 303, 203, 103, 3. So in this case, 
if we remove 4 - 303, 3 will be the first number at the index 3 chain, making 
the search faster. But since we are using a sequential add with rehash(), 
along with a the straightforward hashing method, all cells will have at most 
one item, and removing numbers after 3 won't help the search. 

Using 3, 103, 203, and 303 as an example again, if we don't rehash(),
index 3 will have 303, 203, 103, 3 (assuming no other numbers). Searching for 
303 will go through index 0 to 3. After rehashing, 303 will be at index 103, 
so we would have to go through all the index till index 103 before we find 303. 

"""

from hashset import HashSet
import time
import random


def main():
    # HashSet methods testing
    
    hset1 = HashSet([1,2,3,4,7,8,9,10,12,15])
    hset1.printChains()
    print(hset1)
    print("loadFactor() = ", hset1.loadFactor() )
    print("cellLoadFactor() = ", hset1.cellLoadFactor())
    print("_"*70)
    
    hset1.add(9) # 9 gets added to chain
    hset1.add(14) # 14 triggers rehash()
    hset1.add(30) # 30 gets added to front of chain
    hset1.printChains()   
    print(hset1)
    print("loadFactor() = ", hset1.loadFactor() )
    print("cellLoadFactor() = ", hset1.cellLoadFactor())
    print("_"*70)
    
    # Lab Questions
    
    print("Question 1")
    print("Adding randomly:")
    Q1(True, 500) # True is to randomly add integers
    print("\nAdding in order:")
    Q1(False, 500) #False adds the integers in order
        
    print("\nAdding randomly:")
    Q1(True, 100) # True is to randomly add integers
    print("\nAdding in order:")
    Q1(False, 100) #False adds the integers in order
    
    
    print("_"*70)
    print("Question 2")
    print("Adding 1 to 80 then find 3:")
    Q2(81)
    print("\nAdding 1 to n then find 3:")
    Q2(161)
    
    print("_"*70)
    print("Question 3")
    print("Adding 1 to 80, remove 4 to 80, then find 3:")
    Q3(81)
    print("\nAdding 1 to 80, remove 4 to n, then find 3:")
    Q3(161)
    
    
def Q1(Random, capacity):
    """
    Parameter:
        Random takes in True/False
            if True, insert integers randomly. 
        Capacity takes in initial array capacity. 
    """
    hashSet = HashSet([],capacity)
    listOf400 = list(range(1,401))
    numberLeft = 400
    elapsedTimeTotal = 0
    while numberLeft > 0:
        index = (random.randint(0, numberLeft-1))
        if Random:
            addNumber = listOf400.pop(index)
        else:
            addNumber = listOf400.pop(0)
        startTime = time.time()
        hashSet.add(addNumber)
        endTime = time.time()
        elapsedTimeTotal += round(endTime - startTime, 10)
        numberLeft -= 1
    print("Initial array length:", capacity,"| Final length:",  len(hashSet._array))
    print("Time taken for all add(): ",elapsedTimeTotal)    


def Q2(highestInteger):
    """
    Parameter:
        highestInteger is the max integer to add to the HashSet. 1 - highestInteger. 
    """
    hashSet = HashSet([],100)
    for number in range(1,highestInteger):
        hashSet.add(number)
    startTime = time.time()
    print("3 in hashSet: ",3 in hashSet)
    endTime = time.time()
    elapsedTime = round(endTime - startTime, 10)
    print("Time to find 3: ",elapsedTime)
    print("Array length: ", len(hashSet._array))

    return hashSet

def Q3(highestInteger):
    """
    Parameter:
        highestInteger is the max integer to add to the HashSet. 1 - highestInteger. 
    """
    hashSet = HashSet([],100)
    for number in range(1,highestInteger):
        hashSet.add(number)
    # removing 4 - highestInteger
    for number in range(4, highestInteger):
        hashSet.remove(number)
    startTime = time.time()
    print("3 in hashSet: ", 3 in hashSet)
    endTime = time.time()
    elapsedTime = round(endTime - startTime, 10)
    print("Time to find 3: ", elapsedTime)
    print("Array length: ", len(hashSet._array))

if __name__ == "__main__":
    main()

