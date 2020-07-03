"""
Ricky Cheah
Exercise 4
4/1/2020

Answers: 

1. It will evaluate to true if list mutator methods are used.
Any change to the list made using the iterator will have both mod counts increased,
whereas changes made with list mutator methods will only increase the list's mod count
causing the if statement to return True.

2. In "map(str, self)", the map() function takes an iterable object
and applies the function (str in this case) to each element in the iterable. 
It then returns a map object, which is an iterator. 

The ", ".join portion takes the map object, iterates over it,
and joins all the elements, using ", " in between each two elements. 

3. Please see "Exercise4_Question3_Cheah.pdf"

"""

"""
This is a driver program to test the functionalities of LinkedListIterator class.
Testing codes are taken from testlistiterator.py and modified. 

Original Filename: testlistiterator.py
Original Author: Ken Lambert 
"""

from linkedlist import LinkedList

def test(listType):
    """Expects a list type as an argument and runs some tests
    on objects of that type.""" 
    print("Create a list with 1-9")
    lyst = listType(range(1, 10))
    print("Length:", len(lyst))
    print("Items (first to last):", lyst)
    
    # Create and use a list iterator
    listIterator = lyst.listIterator()
    
    # this is to test the insert method when cursor is undefined, eg: None.  
    print("\nInserting 20 at the end: ", end="")
    listIterator.insert(20)
    print(lyst)
    
    # testing replace method
#    Uncomment below to test for exceptions
#    lyst.pop(2)
     
    print("\nReplacing 20 with 99: ", end="")
    listIterator.last()
    listIterator.previous()
#    listIterator.last()
    listIterator.replace(99)
    print(lyst)
    
    print("Forward traversal: ", end="")
    listIterator.first()
    while listIterator.hasNext(): 
            print(listIterator.next(), end = " ")

    print("\nBackward traversal: ", end="")
    listIterator.last()
    while listIterator.hasPrevious(): 
            print(listIterator.previous(), end=" ")
            
#    Uncomment below to test for exceptions
#    lyst.pop(2)

    print("\nInserting 10 before 3: ", end="")
    listIterator.first()
    for count in range(3):
            listIterator.next()
    listIterator.insert(10)
    print(lyst)
    print("Removing 2: ", end="")
    listIterator.first()
    for count in range(2): 
            listIterator.next()
#    listIterator.first()
    listIterator.remove()
    print(lyst)

    print("_"*70)
    
    # moving iterator backward and element removal 
    print("Removing all items (reverse): Expect []: ", end = "")
    listIterator.last()
    while listIterator.hasPrevious():
        listIterator.previous()
        listIterator.remove()
    print(lyst)
    print("Length:", len(lyst))
    
    print("_"*70)
    
    # create another list to test moving iterator forward and element removal. 
    print("Create a list with 1-10")
    lyst = listType(range(1, 11))
    print("Length:", len(lyst))
    print("Items (first to last):", lyst)
    listIterator = lyst.listIterator()
    
    print("Removing all items (forward): Expect []: ", end = "")
    listIterator.first()
    while listIterator.hasNext():
        listIterator.next()
        listIterator.remove()
    print(lyst)
    print("Length:", len(lyst))
    
test(LinkedList)
    
