'''
Ricky Cheah
Feb 24, 2020
Lab 3 - Option 2

This is a driver function to test the Array class with added functionality.
    Added __eq__, insertItem and removeItem methods. 
'''

from arrays import Array

def main():
    a = Array(5)
    b = Array(5)
    c = Array(6)
    
    b[0] = "b"
    c[0] = "c"
    
    for i in range(len(a)):
        a[i] = i
    print("Array a is", a)
    print("Array b is", b)
    print("Array c is", c)
    
    print(a == b)
    print(a == c)
    
    print("_"*50)
    print("Array a is", a)
    print("Logical size of a is", a.logicalSize())
    print("Inserting item..")
    a.insertItem(3,"foo")
    print(a)
    print("Logical size of a is", a.logicalSize())
    
    print("_"*50)
    print("Removing item..")
    print(a.removeItem(3))
    print("Logical size of a is", a.logicalSize())
    
    
    print(a)

if __name__ == '__main__':
    main()