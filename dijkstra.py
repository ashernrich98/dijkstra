# -*- coding: utf-8 -*-
"""
Asher Rich
Dr. Yu
Computer Networks
11 April 2021
Project
Dijkstra Shortest Path Algorithm
"""

# Dijkstra Algorithm overview can be found in "Project_Rich.pdf" Appendix

# sys = System specific parameters and functions library
# Used for maxsize
import sys

class Data():
    # Define global variables and initialize
    def __init__(self, paths):
        self.P = paths
        self.table = [[0 for column in range(paths)]
                      for row in range(paths)]

    # Function to reproduce switch statement
    # Note: if data to run program is changed this must be updated
    def num2letter(self, val):
        if val == 0:
            return "A"
        if val == 1:
            return "B"
        if val == 2:
            return "C"
        if val == 3:
            return "D"
        if val == 4:
            return "E"
        if val == 5:
            return "F"
        if val == 6:
            return "G"
        if val == 7:
            return "H"
        
    # Function to output values
    def output(self, distance):
        print("Node: Distance from Source")
        for node in range(self.P):
            letter = self.num2letter(node)
            print(letter, ":", distance[node])

    # Function for finding node with smallest distance
    # sptree = shortest path tree
    # node = n
    # adjacent node = a
    def smallestDistance(self, distance, sptree):
        
        # Distance set to equivalent of infinity
        min = sys.maxsize

        # For every node if the distance is less than infinity and the...
        # ... shortest path tree indicates the node has not been visited...
        # ... then update values
        for n in range(self.P):
            if distance[n] < min and sptree[n] == False:
                min = distance[n]
                smallest = n

        return smallest

    # Function to implement the Dijkstra Algorithm
    def dijkstra(self, src):

        distance = [sys.maxsize] * self.P   # Set distances
        distance[src] = 0                   # Set source distance to 0
        sptree = [False] * self.P           # Set tree nodes visited to false
        
        # Main doer of algorithm
        for cout in range(self.P):

            # Set neighbor that has the smallest distance
            a = self.smallestDistance(distance, sptree)

            # Update tree, set node to visited = true
            sptree[a] = True
            # Update smallest distance value only if current distance...
            # ... is bigger than new distance and node is not in tree yet
            for n in range(self.P):
                if self.table[a][n] > 0 and sptree[n] == False and \
                    distance[n] > distance[a] + self.table[a][n]:
                    distance[n] = distance[a] + self.table[a][n]

        self.output(distance)

# Data Necessary to run the program using Figure 5-7
temp = Data(8)

#              A, B, C, D, E, F, G, H
#              0, 1, 2, 3, 4, 5, 6, 7 
temp.table = [[0, 2, 0, 0, 0, 0, 6, 0], # A 0
		      [2, 0, 7, 0, 2, 0, 0, 0], # B 1
		      [0, 7, 0, 3, 0, 3, 0, 0], # C 2
		      [0, 0, 3, 0, 0, 0, 0, 2], # D 3
		      [0, 2, 0, 0, 0, 2, 1, 0], # E 4
   		      [0, 0, 3, 0, 2, 0, 0, 2], # F 5
		      [6, 0, 0, 0, 1, 0, 0, 4], # G 6
		      [0, 0, 0, 2, 0, 2, 4, 0]] # H 7

print(""); print("Node = A")
temp.dijkstra(0)
print(""); print("Node = B")
temp.dijkstra(1)
print(""); print("Node = C")
temp.dijkstra(2)
print(""); print("Node = D")
temp.dijkstra(3)
print(""); print("Node = E")
temp.dijkstra(4)
print(""); print("Node = F")
temp.dijkstra(5)
print(""); print("Node = G")
temp.dijkstra(6)
print(""); print("Node = H")
temp.dijkstra(7)
