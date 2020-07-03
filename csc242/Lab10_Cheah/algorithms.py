"""
File: algorithms.py

Graph processing algorithms
"""

from linkedstack import LinkedStack

def topoSort(g, startLabel = None, endLabel = None):   # Lambert
    g.clearVertexMarks()
    g.clearEdgeMarks()
    
    stack = LinkedStack()
    g.clearVertexMarks()
    for v in g.vertices():
        if not v.isMarked():
            dfs(g, v, stack)
    return stack

def dfs(g, v, stack): # Lambert
    v.setMark()
    for w in g.neighboringVertices(v.getLabel()):
        if not w.isMarked():
            dfs(g, w, stack)
    stack.push(v)

def shortestPaths(g, startLabel, endLabel):
    """
    Computes shortest path from startLabel to endLabel. 
    """
    g.clearVertexMarks()
    g.clearEdgeMarks()
    
    resultDict = {} # This stores the results of each pass 
    startVertex = g.getVertex(startLabel)
    for vertex in g.vertices():
        resultDict[vertex.getLabel()] = [False, 9999, None] # assume 9999 is infinity
        if vertex == startVertex:
            resultDict[vertex.getLabel()] = [True, 0, None]
        else:
            for edge in g.edges():
                # This initializes the dictionary of results
                if edge.getOtherVertex(edge.getToVertex()) == startVertex and edge.getToVertex() == vertex:
                    resultDict[vertex.getLabel()] = [False, edge.getWeight(), startLabel]
    
    # This part completes the result dictionary by going through each vertex
    while True:
        for vertexLabel in resultDict:
            if not resultDict[vertexLabel][0] and resultDict[vertexLabel][1] < 10000: # vertex not included previously
                resultDict[vertexLabel][0] = True
                for edge in g.edges():
                    if edge.getOtherVertex(edge.getToVertex()).getLabel() == vertexLabel and not resultDict[edge.getToVertex().getLabel()][0]:
                        newDistance = edge.getWeight() + resultDict[vertexLabel][1]
                        if newDistance < resultDict[edge.getToVertex().getLabel()][1]:
                            resultDict[edge.getToVertex().getLabel()][1] = newDistance
                            resultDict[edge.getToVertex().getLabel()][2] = vertexLabel   
        
        # check to break out of while loop if all vertices are included.
        vertexIncluded = 0
        for vertexLabel in resultDict:
            if resultDict[vertexLabel][0] == True:
                vertexIncluded += 1
        if vertexIncluded == len(g): 
            break
        
    travelWeight = 0
    travelPath = list(endLabel)
    recordLabel = endLabel # temp placeholder to record path. 
    
    # This part traces the path from start vertex to end vertex and computes weight.
    while True:
        try:
            travelWeight += resultDict[recordLabel][1]
            travelPath.insert(0,resultDict[recordLabel][2])
            recordLabel = resultDict[recordLabel][2]
            
            if recordLabel == startLabel:
                print(f"Path: {' to '.join(travelPath)}, Total Weight = {travelWeight}")
                break
        except:
            print("No path between the two vertices.")
            break
    
    print("_"*70)
    return 0

def spanTree(g, startLabel, endLabel):
    """
    Computes minimum spanning tree of graph. 
    """ 
    g.clearVertexMarks()
    g.clearEdgeMarks()
    
    # set the starting vertex
    firstVertex = g.getVertex(startLabel)
    firstVertex.setMark()
    markedVertex = 1 # used to break while loop
     
    finalEdges = list() # list of edges for minimum tree
    
    while markedVertex != len(g):
        checkTheseEdges = list()  # list of edges to check during each while loop
        for edge in g.edges():
            if not edge.isMarked():
                
                # this checks both the to and from vertex of the edge
                # making sure that only one or the other is marked
                if (edge.getToVertex().isMarked() and not edge.getOtherVertex(edge.getToVertex()).isMarked()) or \
               (not edge.getToVertex().isMarked() and edge.getOtherVertex(edge.getToVertex()).isMarked()):
                   checkTheseEdges.append(edge)

        # checking the edges collected that has only one marked vertex. 
        currentEdge = checkTheseEdges[0]
        for i in range(1, len(checkTheseEdges)):
            if edge.getWeight() < currentEdge.getWeight():
                currentEdge = checkTheseEdges[i]
        currentEdge.setMark()      
        
        # marking both end of edge, one is redundant. 
        currentEdge.getToVertex().setMark()
        currentEdge.getOtherVertex(currentEdge.getToVertex()).setMark()
        
        markedVertex += 1
        finalEdges.append(currentEdge) # appending to shortest edge collection
        
    # printing results
    totalWeight = 0
    for edge in finalEdges:
        totalWeight += edge.getWeight()
        print(str(edge), end = " ")
    print(f"\nWeight: {totalWeight}")
            
    print("_"*70)
    return 0
            