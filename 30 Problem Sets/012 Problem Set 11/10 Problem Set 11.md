
# Fastest Way to Get Around MIT

### Introduction

In this problem set you will write a solution to an optimization problem on how to find the
shortest route from one building to another on the MIT campus given you wish to constrain the
amount of time you will spend walking outdoors (because generally speaking, the nocturnal
beaver... err, the nocturnal MIT engineer... hates the sun).

### Getting Started

Download the files [here]:

[here]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-24-avoiding-statistical-fallacies/ps11.zip

* ps11.py: code skeleton
* graph.py: a set of graph-related data structures (Digraph, Node, and Edge) that you can use
* mit_map.txt: a sample data file that holds the information about an MIT campus map.

### Background

A graph consists of a set of nodes (n1, n2, n3, ....) and a set of edges (e1, e2, e3, ...) where an edge
connects two nodes that are in the graph. The node n1 has children nodes if there exists an edge
from n1 to each child node. In Figure 1, Node “a” has children nodes “b” and “c.”
There are two types of edges: directed and undirected. If the edge is directed, then the edge has a
specific direction going from start to destination node. Graphs with directed edges are called
directed graphs (or **digraph**).

![graph1](graph1.png "Figure 1. Example of a directed graph where each edge has a specific direction.")

If the edge is undirected, also known as bidirectional, then it no longer matters which node is the
start or destination node because you can traverse the edge from one node to the other in either
direction. Essentially, a link in the graph can be represented by a directed edge going from Node
“d” to Node “e” and a directed edge going in the reverse direction.

![graph2](graph2.png "Figure 2. Example of an undirected graph where each edge is bidirectional.")

An edge can also have a weight. If every edge is associated with a real number (edge weight),
then we have weighted graph.

![graph3](graph3.png "Figure 3. Example of an weighted graph where each edge has a weight associated with it.")

In a graph theory problem, the **objective function** is the function to be minimized (or
maximized). For example, choosing the shortest path for airplane flights is an optimization
problem where the objective function is to minimize the distance traveled. The nodes are the
destination airports and edges are the presence of airplane routes between airports. We can add
additional **constraints** on the problem that must be satisfied such as requiring that the plane only
make at most 2 stops along the way from start to end destination. Then the shortest path is only
valid if it satisfies the constraint.

### Introduction

![map](map.png)

Here is the map of the MIT campus that we all know and love. From the text input file,
*mit_map.txt*, you will build a representation of this map in Python using the graph-related data
structures that we provide.

Each line in *mit_map.txt* has 4 pieces of data in it in the following order separated by a single
space (space-delimited): the start building, the destination building, the distance in meters
between the two buildings, and the distance in meters between the two buildings that must be
spent outdoors. For example, suppose the map text file contained the following line:

    10      32      200     40

This means that the map contains an edge from building 10 (start location) to building 32 (end
location) that is 200 meters long, where 40 of those 200 meters are spent outside.
To make the problem interesting, we will say that not every route between a pair of buildings is
bi-directional. For example, it may be possible to get from building 54 (Green building) to
building 56, but not the other way around, because the wind that blows away from the Green
building is too strong.

## Problem 1: Creating the Data Structure Representation

In this problem set, we are dealing with edges that have different weights. In the figure below,
the blue numbers show the cost of traversing an edge in terms of total distance traveled, while
the green numbers show the cost of traversing an edge in terms of distance spent outdoors. Note
that the distance spent outdoors for a single edge is always less than or equal to the total distance
it takes to traverse that edge. Now the cost of going from “a” to “b” to “e” is a total distance
traveled of 22 meters, where 14 of those meters are spent outdoors. These weights are important
when comparing multiple paths because you want to look at the weights associated with the
edges in the path instead of just the number of edges traversed.

![prob1](prob1.png)

In *graph.py*, you’ll find the Digraph, Node, and Edge classes, which do not store information
about weights associated with each edge.

Extend the classes so that it fits our case of a weighted graph. Think about how you can modify
the classes to store the weights shown above. Make modifications directly in graph.py. Hint:
subclass the provided classes to add your own functionality to the new classes. Deciding what
representation to use in order to build up the graph is the most challenging part of the problem
set, so think through the problem carefully.

