'''
Created on Jan 30, 2020
@author: Ricky Cheah
'''

class Library(object):
    '''
    A class to contain the book and patron objects in a library system. 
    Contains methods to: add or remove books and patrons; 
        borrow and return books
        and to show the status of specific book or patron. 
    '''

    #Constructor
    def __init__(self, bookList = []):
        '''
        Creates an empty bookList and patronList by default. 
        '''
        self.bookList = bookList
        self.patronList = []

    def addBook(self, bookID):
        '''
        method takes in a book object to add to library system. 
        Created book objects has to be added before usable!
        '''
        self.bookList.append(bookID)
        
    def addPatron(self, patronID):
        '''
        method to add patron objects to library system. 
        Patron objects has to be added before usable!
        '''
        self.patronList.append(patronID)

    def borrowBook(self, bookID, patronID):
        '''
        Method used when a patron tries to borrow a book. 
        Takes in a book ID and a Patron ID as input. 
        Calls methods in book and patron objects.
        '''
        if bookID not in self.bookList:
            print("Book has not been added to library system!\n")
        elif patronID not in self.patronList:
            print("Patron has not been added to library system!\n")
        else:
            bookID.borrow(patronID)
            patronID.addBook(bookID)
    
    def returnBook(self, bookID):
        '''
        Method used when a patron tries to return a book. 
        Takes in a bookID as input, calls methods in book and Patron objects. 
        '''
        bookID.currentPatron.removeBook(bookID)
        bookID.bookReturn()
        
    def __str__(self): #__str__ should return something, not print something. 
        '''
        Returns the status of all patrons and books. 
        '''
        return(self.showPatrons() + "\n" + self.showBooks())

    def removeBook(self,bookID):
        '''
        method to remove a book object from library.
        '''
        self.bookList.remove(bookID)
        print(f"Book: {bookID.bookName} has been removed from library!\n")
    
    def removePatron(self,patronID):
        '''
        method to remove a patron object from library.
        '''
        self.patronList.remove(patronID)
        print(f"Patron: {patronID.patronName} has been removed from library!\n")
    
    def showPatrons(self):
        '''
        method to lists out all current patrons and their book counts. 
        '''
        patronString = "Patrons: \n"
        for patron in self.patronList:
            patronString += f"{patron.patronName} has {patron.totalBooks} books.\n"
        return patronString
    
    def showBooks(self):
        '''
        method to list out all books and their borrowed and waiting list status. 
        '''
        bookString = "Books: \n"
        for book in self.bookList:
            bookString += f"{book}{'_'*60}\n"
        return bookString
            
    
    def findPatron(self,patronID):
        '''
        method to show the status of a specific patron
        '''
        if patronID not in self.patronList:
            print("Patron has not been added to library system!\n")
        else:
            print(f"PATRON STATUS:\n{patronID}")
    
    def findBook(self,bookID):
        '''
        method to show the status of a specific book. 
        '''
        if bookID not in self.bookList:
            print("Patron has not been added to library system!\n")
        else:
            print(f"BOOK STATUS:\n{bookID}")
