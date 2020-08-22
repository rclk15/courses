"""
Ricky Cheah
7/10/2020
Lab 5
"""

from partition import Partition
from heap import Heap # modified From lab 4

def main():
    # This runs in2_edges.txt and in3_edges.txt
    for i in range(2, 4):
        KruskalMST(f'in{i}_edges.txt', f'out{i}_edges.txt')

def KruskalMST(inFile, outFile):
    '''
    Provided with an @inFile containing the edges of a weighted graph,
    this function processes the edges and finds a minimum spanning tree.
    Writes results to @outFile. 
    
    initialGraphEdges is a .txt file containing all the edges of the initial graph 
    and their respective weights.
    '''
    print(f"Input file = {inFile}, Output file = {outFile}.")
    
    MST = [] # the edges in the final MST.
    MST_weight = 0 # start with 0 weight
    priorityEdges = Heap() # This is a min-heap, sorted based on the weight of edges.
    forest = Partition() # This is used aid the creation, and merging of subgraph. 
    vertices = {} # This is used to store all the vertices from the graph
    
    totalEdges = 0
    totalWeight = 0
    
    f = open(inFile, 'r')
    g = open(outFile, 'w')
    
    startingEdges = f.readlines()
    f.close()

    startingEdges.pop(0) # this removes the string description of inFile
    g.write("Graph edges: vertice1, vertice2, weight of the edge\n\n")
    
    # This portion processes data from inFile creates single node subgraphs
    for i in range(len(startingEdges)):
        
        extracted = startingEdges[i].split()
        weight, vertex1, vertex2 = int(extracted[2]), int(extracted[0]), int(extracted[1])
        startingEdges[i] = (weight, (vertex1, vertex2)) # storing edges as nested tuple
        
        # creation of single node subgraphs
        if vertex1 not in vertices:
            vertices[vertex1] = forest.createGroup(vertex1)
        if vertex2 not in vertices:
            vertices[vertex2] = forest.createGroup(vertex2)
        
        totalEdges += 1
        totalWeight += weight
        g.write(f"edge: {vertex1}, {vertex2}, {weight} \n")

    # This inserts the edges of our graph into the min-heap, according to the edges' weights.
    for edge in startingEdges:
        priorityEdges.insert(edge)

    vertexCount = len(vertices)

    g.write("\nKruskal spanning tree edges: vertice1, vertice2, weight of the edge\n\n")
    
    # this portion creates the MST by going through all the edges and by merging subgraphs
    while len(MST) != vertexCount - 1 and priorityEdges: # edge number is one less
        minEdge = priorityEdges.deleteMin()
        weight = minEdge[0]
        vertexA = minEdge[1][0]
        vertexB = minEdge[1][1]
        
        a = forest.findParent(vertices[vertexA])
        b = forest.findParent(vertices[vertexB])
        
        # this portion runs if two sub-graphs have different parents (not linked by an edge)
        # merges the two subgraphs. 
        if a != b:
            MST.append(minEdge)
            g.write(f"edge: {vertexA}, {vertexB}, {weight} \n")
            MST_weight += minEdge[0]
            forest.positionUnion(a,b)

    print(f"Total initial edges: {totalEdges}. Total initial weight: {totalWeight}.")
    print(f"Final MST edges: {len(MST)}. Final MST weight: {MST_weight}\n")

    g.write(f"\nKruskal spanning tree weight is {MST_weight}.")
    
    g.close()
        

if __name__ == "__main__":
    main()