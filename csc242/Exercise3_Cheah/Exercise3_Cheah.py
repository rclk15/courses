'''
Ricky Cheah
Mar 6, 2020

This is a driver program modified from Exercise 3 specifications
    to verify functionality of the LinkedBagSub class after LinkedBag 
    was made a sub-class of AbstractBag. Also tested is the Ball Class. 

To trace what methods are called, and from where,
change AbstractBag.TRACE to True. Can be used for debugging purposes. 



'''

from ball import Ball
from linkedbagsub import LinkedBagSub

def main():
    aBag = LinkedBagSub()
    anotherBag = LinkedBagSub()
    print("length of aBag is",len(aBag))            #abstractbag's __len__
    ball1 = Ball("Red", "round")
    ball2 = Ball("Green", "infinity")
    ball3 = Ball("Blue", "mobius")
    ball4 = Ball("Yellow", "hyperboloid")
    myBag = LinkedBagSub([ball1, ball2, ball3])     #linkedbag's add
    print(myBag, "with length =", str(len(myBag)))  #linkedbag's __iter__ and abstractbag's __str__
    myBag.clear()                                   #linkedbag's clear
    print(myBag, "with length =", str(len(myBag)))
    sep()
    
    myBag.add(Ball("Black", "torus"))
    anotherBag.add(ball4)                           #linkedbag's add
    print(myBag, "with length =", str(len(myBag)))
    print(anotherBag, "with length =", str(len(anotherBag)))
    sep()
    
    myBag += anotherBag                             #abstractbag's __add__
    print(myBag, "with length =", str(len(myBag)))
    sep()
    
    for bagItem in myBag:                           #linkedbag's __iter__
        print(bagItem)
        
    if ball4 in myBag: 
        print("Ball4 is in the bag.")
    sep()        
    
    print(myBag == aBag)                             #abstractbag's __eq__ and __Len__
    myBag.clear()                                    #linkedbag's clear
    print(myBag == aBag) 
    sep()
    
    myBag.add(ball4)
    print(myBag)
    clonedBag = myBag.clone()                         #abstractbag's clone
    print("myBag == clonedBag,", myBag == clonedBag)
    print("myBag is clonedBag,", myBag is clonedBag)
    sep()  
    
    print(myBag.isEmpty())                            #abstractbag's isEmpty    
    print(myBag)
    myBag.remove(ball4)                               #linkedbag's remove
    print(myBag.isEmpty())
    myBag.remove(ball1)                               #linkedbag's remove, not in bag
    sep()

def sep():
    '''
    prints out a linebreak 
    '''
    print("_"*70)
    
if __name__ == '__main__':
    main()