"""
Ricky Cheah
Lab 10
5/11/2020

2. Option 3
# myGraph.gph

3. Option 4

4. Option 5
Comment:
Can start with any vertices, code checks both forward and backward directions of edges.
    Eg: can start with vertex E.

5. 
A B C E D
A B C D E

Comment:
Since all edges must point forward,
D and E must come after B, C and A, and their positions are interchangeable.
C must come after B, A must be the first. 
"""

from view import GraphDemoView

GraphDemoView().run()

