
# Simulating the Spread of Disease and Virus Population

### Introduction

In this problem set, using Python and matplotlib you will design and implement a stochastic
simulation of patient and virus population dynamics, and reach conclusions about treatment
regimens based on the simulation results.

You should submit 3 files for this problem set: your code in ps7.py and ps7b.py, and a write-
up in txt format called writeup.txt.


### Getting Started

Download the py file [here].

[here]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-16-using-randomness-to-solve-non-random-problems/ps7.py

For this lab, you will be using matplotlib to plot the results of simulation runs, which you should
already have from Problem Set 6.

### Background: Viruses, Drug Treatments, and Computational Models

Viruses such as HIV and H1N1 represent a significant challenge to modern medicine. One of the
reasons that they are so difficult to treat is because of their ability to evolve.

As you may know from introductory biology classes, the traits of an organism are determined by
its genetic code. When organisms reproduce, their offspring will inherit genetic information from
their parent. This genetic information will be modified, either because of mixing of the two
parents’ genetic information, or through mutations in the genome replication process, thus
introducing diversity into a population.

Viruses are no exception. Two characteristics of viruses make them particularly difficult to treat.
The first is that their replication mechanism often lacks the error checking mechanisms that are
present in more complex organisms. This speeds up the rate of mutation. Secondly, viruses
replicate extremely quickly, orders of magnitude faster than humans. Thus, while we may be
used to thinking of evolution as a process which occurs over long time scales, populations of
viruses can undergo substantial evolutionary changes within a single patient over the course of
treatment.

These two characteristics allow a virus population to quickly acquire genetic resistance to
therapy. In this problem set, we will make use of simulations to explore the effect of introducing
drugs on the virus population and determine how best to address these treatment challenges
within a simplified model.

Computational modeling has played an important role in the study of viruses such as HIV (for
example, see [this paper], by MIT graduate David Ho). In this problem set, we will implement a
highly simplified stochastic model of virus population dynamics. Many details have been swept
under the rug (host cells are not explicitly modeled and the size of the population is several
orders of magnitude less than the size of actual virus populations). Nevertheless, our model
exhibits biologically relevant characteristics and will give you a chance to analyze and interpret
interesting simulation data.

[this paper]: http://biowiki.org/%7Eyam/refs/PerelsonEtAl1996.pdf

## Spread of a Virus in a Person

In reality, diseases are caused by viruses and have to be treated with medicine, so in the
remainder of this problem set, we’ll be looking at a detailed simulation of the spread of a virus
within a Person. We’ve provided you with skeleton code in ps7.py.

### Problem 1

