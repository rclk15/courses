"""
Ricky Cheah
Lab 7
3/28/2020

This driver program solves maze.txt using the queue method first, and then using
the stack method. After solving the maze, the number of choice points used is displayed,
along with the percentage of blank spots visisted while solving the maze. 

Detailed Explanation:
    
The stack method (last in first out) tends to be more efficient and results in
fewer choice points (less visited spots overall) when T is far away from P.
This is because this method focuses on exploring one path at a time while
going further and further away from P, which normally gets it closer to T. 
This method also focuses on only one path at a time, instead of advancing multiple paths
as with the queue method.

The best case for this method will be a straight sprint towards T, though
this is extremely difficult as it requires the correct path choice at every turn, 
but it is possible depending on the order in which we check a location's surrounding. (SEE stack-best.txt)
The worst case for this method is the reverse of the best case, in that
even if T is right next to P, the program will take the wrong path at every turn, 
checking points further and further away. (SEE stack-worst.txt)

The queue method (first in first out) will have multiple paths going at the same time.
All available paths will take turns to take one step forward at a time, 
resulting in a multi-prong advancement from P, and from every fork found. 

The best cases for this method will be when T is close to P, as every possible 
path closest to P will be combed through. The worst case for stack could
be solved easily with queue. (SEE queue-best-stack-worst)
The worst case for this method will be when T is the absolute furthest point away from P, and 
in this case all blank points will be visited before P is found. (SEE queue-worst.txt)

It is hard to conclusively state which method is best, as it depends on the layout
of the maze, and the position of T in the maze. In the case of the stack method,
the order in which we check the four directions in the function checkSurrounding()
will influence whether we will get a best or worst case scenario.
"""
import mazeQueue, mazeStack

def main():
    
    #this maze being solved illustrates stack's worst case scenario. 
    
    print("Now solving the maze using queues.")
    mazeQueue.main()
    print("_"*70 + "\n" + "_"*70 + "\n")
    print("Now solving the maze using stacks.")
    mazeStack.main()

if __name__ == "__main__":
    main()