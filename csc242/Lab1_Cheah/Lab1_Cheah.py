'''
Created on Jan 30, 2020
@author: Ricky Cheah

This is a driver program taken and modified from Lab 1's specification.
Purpose: to verify the correct implementation of library.py, patron.py and book.py modules. 
The Library object manipulates Book and Patron objects and calls their methods to borrow and return books. 
'''

from book import Book
from patron import Patron
from library import Library

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
    book5 = Book("Siddhartha", "Hesse") 
    book6 = Book("Python Fundamentals", "Lambert") #Book not added to library
    patron1 = Patron("Ricky")
    patron2 = Patron("Bernard")
    patron3 = Patron("Annie")
    patron4 = Patron("Bender") 
    patron5 = Patron("Samuel") #Patron not added to library

    myLibrary = Library()
    myLibrary.addBook(book1)
    myLibrary.addBook(book2)
    myLibrary.addBook(book3)
    myLibrary.addBook(book4) 
    myLibrary.addBook(book5) 
    
    myLibrary.addPatron(patron1)
    myLibrary.addPatron(patron2)
    myLibrary.addPatron(patron3)
    myLibrary.addPatron(patron4)

    myLibrary.borrowBook(book1, patron1)
    myLibrary.borrowBook(book2, patron1)
    myLibrary.borrowBook(book3, patron1)
    myLibrary.borrowBook(book4, patron3)
    myLibrary.borrowBook(book4, patron1) #patron1 tries to borrow 4th book, not added to waiting list
    myLibrary.borrowBook(book1, patron2) #patron2 added to waiting list 
    myLibrary.borrowBook(book6, patron1) #book not added
    myLibrary.borrowBook(book1, patron5) #patron not added
     
    myLibrary.returnBook(book1) #book1 returned by patron1, waiting patron borrows book automatically. 
    myLibrary.borrowBook(book4, patron1) #patron1 now has 2 books, tries to borrow an already borrowed book.  
        
    myLibrary.findPatron(patron2) #shows patron2 status
    myLibrary.findBook(book4) #shows book4 status
    
    separator()   
    print(myLibrary)
    separator() 
    myLibrary.removeBook(book5)
    myLibrary.removePatron(patron4)
    
    separator() 
    print(myLibrary) #to show book5 (Siddhartha) and patron4 (Bender) has been removed. 


if __name__ == '__main__':
    main()
