'''
Ricky Cheah
Feb 26, 2020
Lab 4

This is a driver function to test the clone method in ArrayBag and LinkedBag
classes. 

'''
from arraybag import ArrayBag
from linkedbag import LinkedBag

print("Testing clone method on ArrayBag.")
arrayBag1 = ArrayBag([2, 3, 4, "abcd"])
print("arrayBag1 is", arrayBag1)
print("\nExecuting arrayBag2 = arrayBag1.clone()")

arrayBag2 = arrayBag1.clone()
print("arrayBag2 is", arrayBag2)
print()
print("arrayBag2 == arrayBag1:",arrayBag2 == arrayBag1)
print("arrayBag2 is arrayBag1:",arrayBag2 is arrayBag1)


print("_"*70)

print("Testing clone method on LinkedBag.")
linkedBag1 = LinkedBag([4, 5, 6, "defg"]) #element order will be reversed in list
print("linkedBag1 is", linkedBag1)
print("\nExecuting linkedBag2 = linkedBag1.clone()")

linkedBag2 = linkedBag1.clone()
print("linkedBag2 is", linkedBag2)
print()
print("linkedBag2 == linkedBag1:",linkedBag2 == linkedBag1)
print("linkedBag2 is linkedBag1:",linkedBag2 is linkedBag1)
