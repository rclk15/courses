"""
Ricky Cheah
Exercise 5
4/27/2020

 This driver tests both linear and quadratic probing when inserting new items.
 Other mthods tested: 
     __contains__
     get()
     remove()

"""

from hashtable import HashTable

def main():

    # linear probing
    table1 = HashTable()
    table1.insert(3) # index 3
    table1.insert(4) # index 4
    table1.insert(13) # probes from 3, 4, to index 5
    print(f"Home for 13 is {table1._homeIndex}, probeCount = {table1._probeCount}")
    table1.insert(9) 
    print(table1)
    print("Current loadFactor =", table1.loadFactor())
    table1.insert(3) # insert duplicate
    print("3 in table1:", 3 in table1) # search for existing item (__contains__)
    print("6 in table1:", 6 in table1) # search for non-existing item (__contains__)
    print("get(3) =", table1.get(3)) # get index for existing item
    print("get(3) =", table1.get(6)) # get index for non-existing item
    print("remove(3) =", table1.remove(3)) # remove existing item  
    print("remove(10) =", table1.remove(10))  # remove non-existing item
    print(table1)            
    
    print("_"*60)
    
    # quadratic probing
    table2 = HashTable(10, hash, False)
    table2.insert(3) # index 3
    table2.insert(4) # index 4
    table2.insert(7) # index 7
    table2.insert(13) # probe wraps around from index 3, 4, 7 to index 2
    print(f"Home for 13 is {table2._homeIndex}, probeCount = {table2._probeCount}")
    print(table2)
    print("Current loadFactor =", table2.loadFactor())
    print("get(3) =", table2.get(3)) # get index for existing item
    print("get(3) =", table2.get(6)) # get index for non-existing item
    print("remove(3) =", table2.remove(3)) # remove existing item  
    print("remove(10) =", table2.remove(10))  # remove non-existing item
    print(table2)   


if __name__ == "__main__":
    main()

