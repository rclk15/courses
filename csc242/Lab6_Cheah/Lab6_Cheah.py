"""
Ricky Cheah
3/19/2020

This Module, in the main() function, takes in a maze.txt file and creates a solution 
of the maze called mazesolution.txt in the same folder. 
"""

from linkedstack import LinkedStack 
#LinkedStack instead of ArrayStack b/c don't need random access of arrays

def main():
    
    inFile = open('maze1.maz', "r") #insert maze file name here. 
    
    open('mazesolution.txt', "w").close() #this "resets" the output file each time
    outFile = open('mazesolution.txt', "r+") #open in write and read mode "r+"
    
    #temporary list to store our maze (list is mutable, we can insert a "." after visiting)
        #way around this is to create an array to store locations visited and
        #in CheckSurrounding, check if the new location is in the visited array.
    mazeList = list() 
    #this reads the input maze file and converts it to a list() format. 
    inputRows = inFile.readlines()
    for row in inputRows:
        mazeList.append(list(row)) #converting the rows to list
    inFile.close()
    
    #finding the size of the maze
    ymax = len(mazeList)
    xmax = len(mazeList[0])
        
    def findP():
        """
        This function finds "P" in the maze and returns its position.
        """
        for y in range(ymax):
            for x in range(xmax):
                if mazeList[y][x] == "P":
                   return(y,x)
        print("There is no 'P' in the maze!")

    def findT():
        """
        This function finds "T" in the maze and returns its position.
        """
        for y in range(ymax):
            for x in range(xmax):
                if mazeList[y][x] == "T":
                   return(y,x)
        print("There is no 'T' in the maze!")
    
    def checkSurrounding(currentY, currentX):
        """
        This function takes in a location, and checks its surroundings
        to check if a path is available. 
        """
        global FOUND #This variable keeps track if we found "T"
        FOUND = False 
        
        #This portion checks the EAST of the current position.
        if currentX < xmax-1:
            if mazeList[currentY][currentX+1] == " ":
                toVisit.push((currentY, currentX+1))
            elif mazeList[currentY][currentX+1] == "T":
                FOUND = True #Changing FOUND to True will end the while loop

        #This checks the WEST of the current position.
        if currentX > 0:
            if mazeList[currentY][currentX-1] == " ":
                toVisit.push((currentY, currentX-1))
            elif mazeList[currentY][currentX-1] == "T":
                FOUND = True
                
        #This checks the NORTH of the current position     
        if currentY < ymax-1:
            if mazeList[currentY+1][currentX] == " ":
                toVisit.push((currentY+1, currentX))
            elif mazeList[currentY+1][currentX] == "T":
                FOUND = True
                
        #This checks the SOUTH of the current position      
        if currentY > 0:
            if mazeList[currentY-1][currentX] == " ":
                toVisit.push((currentY-1, currentX))
            elif mazeList[currentY-1][currentX] == "T":
                FOUND = True
    
    toVisit = LinkedStack() #Storing locations to be visited 
    startP = findP() #Storing P's location
    print("P is here: ", startP) #This is assuming there are indeed a P and a T
    print("T is here: ", findT()) 
    checkSurrounding(startP[0], startP[1]) #to populate toVisit the first time
    
    #This while loop iterates as long as toVisit is not empty, and Found is False. 
    while toVisit and not FOUND:
        visitHere = toVisit.pop()
        checkSurrounding(visitHere[0], visitHere[1])
        mazeList[visitHere[0]][visitHere[1]] = "." #marks the position we visisted
    
    if FOUND:
        print("There is a solution to this maze.")
    else:
        print("There is no solution to this maze.")
        
    print("_"*70 + "\n")

    #this part converts our maze from a list format back to a string format 
    #and writes into our solution file. 
    for row in mazeList:
        tempStr = ""
        for ch in row:
            tempStr += ch
        outFile.write(tempStr)
    #this completes writing to the file. 

    outFile.seek(0) #this moves the cursor back to the beginning for reading. 
    outputRows = outFile.readlines()
    for row in outputRows:
        print(row)
    outFile.close()

if __name__ == "__main__":
    main()