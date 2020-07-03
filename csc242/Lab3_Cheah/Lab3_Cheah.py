'''
Ricky Cheah
Feb 23, 2020
Lab 3 - Option 1

newSinglyLinked = function to create a circular singly-linked-list.
makeTwoWay = function to create a new circular double-linked-list from a singly-linked.
twoWayTester = function to test ability to traverse a circular doubly-linked-list back and forth.
'''
from node import Node, TwoWayNode

def main():
    
    singlyListHeadTail = newSinglyLinked(6) #creates singly linked list
    
    #creates doubly linked list from a singly linked list
    doubleListHeadTail = makeTwoWay(singlyListHeadTail[0]) #takes the head only
    twoWayTester(doubleListHeadTail[0],doubleListHeadTail[1]) #tests the links of the doubly linked list 
    
def makeTwoWay(listHead):
    '''
    This function takes in the "head" of a singly-linked-list, creates a
    doubly-linked-list with the same data, and returns the head and tail of the 
    created list. 
    
    @param listHead: the pointer to the first node of a singly-linked-list 
    '''

    probe = listHead
    newListHead = TwoWayNode(probe.data) #creates first node and point to it
    tempPointer = newListHead #pointer used to move forward while creating
    newListTail = None #to point at the end of the list later
    while probe.next != None and probe.next != listHead:
        probe = probe.next
        tempPointer.next = TwoWayNode(probe.data, tempPointer, None)
        tempPointer = tempPointer.next
    newListTail = tempPointer #assigns tail pointer to last node
    tempPointer.next = newListHead #points the "next" pointer of last node to first node
    newListHead.previous = newListTail #points the "previous" pointer of first node to last node
    print("Circular Doubly linked list created.")
    return (newListHead, newListTail)

def newSinglyLinked(listLength):
    '''
    This function creates a singly-linked-list of length listLength
    with the node's position(index) as the node data. 
    Returns the head and tail of the created list. 
    
    @param listLength: The length of the list to be created 
    '''
    headSingle = None
    tailSingle = None
    tempPointer = None #pointer used to move forward while creating
    for count in range(1, listLength + 1):
        if count == 1: #creating first node
            headSingle = Node(count, None)
            tempPointer = headSingle
        else: #create the rest of the nodes
            tempPointer.next = Node(count, None)
            tempPointer = tempPointer.next  
    tailSingle = tempPointer
    tempPointer.next = headSingle #points the "next" of last node to first node
    print("Circular Singly linked list of size", listLength, "created.")
    return (headSingle,tailSingle)

def twoWayTester(listHead, listTail):
    '''
    This function takes in the head and tail of a doubly-linked-list, traverses to 
    the end of the list while printing each node's data.
    Then it traverses back towards the head of the list while still printing
    each node's data. 
    
    @param listHead: The head of the list to be traversed. 
    @param listTail: The tail of the list to be traversed.
    '''
    probe = listHead #assigns node to first node

    print("Now traversing towards the end of the doubly linked list.")
    print(probe.data) #prints the first data before going into while loop

    while probe.next != None and probe.next != listHead:
        probe = probe.next
        print(probe.data)
    print("Reached the end. \nNow traversing towards the head.")
    
    probe = listTail #assigns probe to last node
    print(probe.data)
    while probe.previous != None and probe.previous != listHead:
        probe = probe.previous
        print(probe.data)  
    probe = probe.previous
    print(probe.data)   
    print("Reached the head.")
    
if __name__ == '__main__':
    main()