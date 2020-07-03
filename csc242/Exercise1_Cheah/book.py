'''
Created on Jan 23, 2020
@author: Ricky Cheah

This module contains the Book class and its associated methods. 
'''


class Book:
    '''
    A class to hold information such as the book's name, author's name,
    whether the book is borrowed, current patron in possession of the book, 
    and the list of patrons waiting. 
    '''


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
        Method called when a patron tries to borrow this book.
        If currently borrowed, patron will be added to waiting list. 
        If over max books, does nothing (handled by Patron's addBook method).
        '''
        if not self.borrowed:
            if len(patronName.bookList) < 3: 
                self.currentPatron = patronName
                print(f"{patronName.patronName} successfully borrowed {self.bookName}. "
                      f"({len(patronName.bookList)+1} books)\n")
        else:
            self.waitingPatron.append(patronName)
    
        
    def __str__(self):
        '''
        Returns bookName and bookAuthor, along with currentPatron.
        Lists out waitingPatron
        '''
        waitingString = ""
        if self.waitingPatron:
            waitingString += "\nWaiting:\n"
            for i in range(len(self.waitingPatron)):
                waitingString += (f"{i + 1}. {self.waitingPatron[i].patronName} "
                                  f"({self.waitingPatron[i].totalBooks} books)\n")

        return (f"{self.bookName}, {self.bookAuthor} in care of: {self.currentPatron.patronName} ({self.currentPatron.totalBooks} books)\n\
                {waitingString}")