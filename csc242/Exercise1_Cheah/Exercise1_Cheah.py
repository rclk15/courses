'''
Created on Jan 23, 2020
@author: Ricky Cheah

This is a driver program taken and modified from Exercise 1's specification.
Purpose: to verify the correct implementation of patron.py and book.py modules. 
Book and Patron objects are created and their methods tested. 
'''

from book import Book
from patron import Patron

def separator():
    '''
    prints out a line to separate information. 
    '''
    print('*' * 80)
    

def main():
    '''
    main function to create Book and Patron objects. 
    Books are then "borrowed" by Patrons.
    '''
    book1 = Book("Brave New World", "Huxley")
    book2 = Book("Leviathan Wakes", "Corey")
    book3 = Book("East of Eden", "Steinbeck")
    book4 = Book("The Last Lecture", "Pausch")
    patron1 = Patron("Ricky")
    patron2 = Patron("Bernard")
    patron3 = Patron("Annie")
    patron4 = Patron("Samuel")
    
    book1.borrow(patron1)
    patron1.addBook(book1)
    
    book1.borrow(patron2)
    patron2.addBook(book1)
    
    book1.borrow(patron3)
    patron3.addBook(book1)
    
    book2.borrow(patron1)
    patron1.addBook(book2)
    
    book3.borrow(patron1)
    patron1.addBook(book3)
    
    book4.borrow(patron1) 
    patron1.addBook(book4) #patron1 tries to borrow 4th book. 

    book4.borrow(patron2)  
    patron2.addBook(book4)
    
    book3.borrow(patron2)  
    patron2.addBook(book3)
    

    
    separator()
    print("Book1 - " + str(book1))
    separator()
    print("Book2 - " + str(book2))  
    separator()
    print("Book3 - " + str(book3)) 
    separator()
    print("Book4 - " + str(book4))     
    separator()
    print("Patron1 - " + str(patron1)) 
    separator()   
    print("Patron2 - " + str(patron2)) 
    separator()
    print("Patron3 - " + str(patron3)) 
    separator()
    print("Patron4 - " + str(patron4))


if __name__ == '__main__':
    main()

    