'''
Created on Jan 23, 2020
@author: Ricky Cheah

This module contains the Patron class and its associated methods. 
'''

class Patron:
    '''
    A class to hold information like the patron's name, 
    total number of books they have, the IDs of the book they have,
    and patrons waiting for the book.
    '''
    
    # Constructor
    def __init__(self, patronName):
        '''
        Sets up a new patron with name, 0 currently borrowed book, 
        a books list, and a waited books list.
        '''
        self.patronName = patronName
        self.totalBooks = 0
        self.bookList = []
        self.waitingFor = []

    def borrowedBooks(self):
        '''
        method to list out the books currently borrowed
        '''
        if self.totalBooks == 0:
            return f"{self.patronName} does not have any books.\n"
        else:
            borrowedString = ""
            for i in range(self.totalBooks):
                borrowedString += f"{i + 1}. {self.bookList[i].bookName}\n"
            return f"{self.patronName} currently has: \n{borrowedString}"
    
    def waitingForBooks(self):
        '''
        list out books waited for
        '''
        waitingString = ""
        if self.waitingFor:
            waitingString = f"\nWaiting for: \n{waitingString}"
            for i in range(len(self.waitingFor)):
                waitingString += f"{i + 1}. {self.waitingFor[i]}\n"
        return waitingString
        
    def addBook(self, bookID):
        '''
        method to check if max number of books exceeded. Displays error message if exceeded.
            Else, increases book counter and add book to patron's borrowed list. 
        '''
        if self.totalBooks < 3:
            if bookID.borrowed == False:
                self.totalBooks += 1 
                self.bookList.append(bookID)
                bookID.borrowed = True
            else:
                self.waitingFor.append(bookID.bookName)
                print(f"{bookID.bookName} has already been borrowed by {bookID.currentPatron.patronName}.\
                      \n{self.patronName} added to the waiting list. Position: {len(bookID.waitingPatron)}\n")
        else:
            print(f"Max number of books reached! \n{self.borrowedBooks()}")
        
    def __str__(self):
        '''
        Returns the string representation of patronName and totalBooks
        '''
        return f"{self.borrowedBooks()}{self.waitingForBooks()}"