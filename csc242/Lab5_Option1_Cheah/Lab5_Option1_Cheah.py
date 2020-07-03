
"""
Ricky Cheah
3/11/2020

This is a driver program to test __contains__ and remove methods in ArrayBag.
"""

from arraybag import ArrayBag

def main():
    bag1 = ArrayBag([1,2,3,4,5,6])

    print("bag1 is", bag1)

    bag2 = ArrayBag([7, 8, 9, 10, 11])
    print("bag2 is", bag2)
    
    bag1 = bag1 + bag2
    print("bag1 after bag1 + bag2 =", bag1, "length =", len(bag1))
    
    sep()
    
    for number in range(1,12):
        if number in bag1:
            bag1.remove(number)
    
    print("bag1 after removing every number in range(1,12) =", bag1, "length =", (len(bag1)))
    bag1.remove(0)
    
def sep():
    print("_"*60)
        
if __name__ == "__main__":
    main()
