'''
Created: Jan 23, 2020
Modified: Jan 30, 2020
@author: Ricky Cheah

This module contains the Book class and its associated methods. 
'''


class Book:
    '''
    A class to hold information such as the book's name, author's name,
    whether the book is borrowed, current patron in possession of the book, 
    and the list of patrons waiting. 
    '''

    #Constructor
    def __init__(self, bookName, bookAuthor):
        '''
        Sets up a new book ID with the book's name and the author's name as parameters.
        Also initializes current patron(string), waiting patron(list), borrowed status. 
        '''
        self.bookName = bookName
        self.bookAuthor = bookAuthor
        self.borrowed = False
        self.currentPatron = ""
        self.waitingPatron = []
        
    def borrow(self, patronName):
        '''
        Method called (by library object) when a patron tries to borrow this book.
        If currently borrowed, patron will be added to waiting list. 
        If over max books, does nothing (handled by Patron's addBook method).
        '''
        if len(patronName.bookList) < 3:
            if not self.borrowed:
     
                self.currentPatron = patronName
                print(f"{patronName.patronName} successfully borrowed {self.bookName}. "
                      f"({len(patronName.bookList)+1} books)\n")
            else:
                self.waitingPatron.append(patronName)
    
    def bookReturn(self):
        '''
        Method called (by library object) when a patron returns a book.
        If there is a waiting patron, he/she automatically borrows the returned book. 
        '''
        if self.borrowed:
            self.borrowed = False
            print(f"{self.currentPatron.patronName} has returned {self.bookName}.")
            if self.waitingPatron:  #if there is a patron waiting, borrows book automatically. 
                nextPatron = self.waitingPatron.pop(0)
                self.borrow(nextPatron)
                nextPatron.addBook(self)
                
    
    def strReturn(self):
        '''
        Helper function to __str__. Organizes the book status into a String object.  
        '''
        returnString = ""
        if self.borrowed == False:
            returnString += f"{self.bookName}, {self.bookAuthor} has not been borrowed.\n"
        else: 
            returnString += f"{self.bookName}, {self.bookAuthor} in care of: {self.currentPatron.patronName} ({self.currentPatron.totalBooks} books)\n"
        if self.waitingPatron:
            returnString += "Waiting:\n"
            for i in range(len(self.waitingPatron)):
                returnString += (f"{i + 1}. {self.waitingPatron[i].patronName} "
                                  f"({self.waitingPatron[i].totalBooks} books)\n")        
        return returnString
    
    def __str__(self):
        '''
        Returns bookName and bookAuthor, along with currentPatron.
        Lists out waitingPatron
        '''
        return self.strReturn()
