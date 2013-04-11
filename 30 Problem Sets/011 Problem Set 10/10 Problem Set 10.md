
# Clustering

### Introduction

For this problem set, you will be using k-means clustering to process and analyze data.

You will have to produce only a small amount of code, but you should be sure to understand the
code that has been given to you.

You may work with other students. However, each student should write up and hand in his or her
assignment separately. **Be sure to indicate with whom you have worked.**

Getting Started

Download the zip [here], containing:

* ps10.py
* counties.txt

[here]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-3/lecture-22-using-graphs-to-model-problems-part-2/ps10.zip

**TODO: Submit all your answers to the written questions in a single file called ps10_writeup.pdf.**

### Background Overview

Every decade, the United States Census takes place. The census collects a lot of information
from the population around the United States. In this problem set, we are going to use k-means
clustering to analyze this information.

**It is essential in this problem set to not try running everything at once.** The data set is very large,
and some functions will take a long time to run. You should test out each element of the code
you are asked to write and/or understand. First, test your code on a sample data set and see if you
get the expected results. Once you are comfortable with the outcome, you should produce the
graphs for your writeup using the full data set. **Running this code may take a while!**

To help you, we’ve setup the starter code to load two global sets, “points”, which contains all the
data in *counties.txt*, and “testPoints”, which has only a tenth of the full data (this should be small
enough for most of your tests to run fairly quickly).

## Problem 0: Provided classes and functions

In *ps10.py*, we’ve provided the following classes that you will use in this problem set:

* __Point Class__: represents the the data points
* __County Class__: represents the counties and contains a method that returns the distance
between two clusters. Also extends the Point class.
* __Cluster Class__: represents the clusters

In addition to the above, we’ve provided the following functions that you will use in this
problem set:

* __kmeans()__: produces a list of clusters and the maximum distance of any point in a cluster
to its centroid
* __readCountyData()__: takes a filename and number of features to import. Returns the
names, list of data points, and the maximum values
* __buildCountyPoints()__: uses readCountyData to create County instances given each
county from readCountyData
* __randomPartition()__: partitions a list into two lists

Finally, there is one sample function to get you started:

* __test()__: takes in a set of data points, uses kmeans to cluster them, and gives a histogram of
some average values.

**Read ps10.py carefully before starting, so that you understand the provided code and its
capabilities.**

