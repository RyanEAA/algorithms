import math
from timeit import default_timer as timer
import random
import matplotlib.pyplot as plt
import numpy as np
import timeit

stepcounter = 0
def merging(leftCabinet, rightCabinet):
    global stepcounter
    
    # Merge sort the left and right cabinets
    leftCabinet = mergesort(leftCabinet)
    rightCabinet = mergesort(rightCabinet)

    newCabinet = []
    
    while min(len(leftCabinet), len(rightCabinet)) > 0:
        
        if leftCabinet[0] > rightCabinet[0]:
            to_insert = rightCabinet.pop(0)
            newCabinet.append(to_insert)
            stepcounter += 1
        elif leftCabinet[0] <= rightCabinet[0]:
            to_insert = leftCabinet.pop(0)
            newCabinet.append(to_insert)
            stepcounter += 1

    if len(leftCabinet) > 0:
        for i in leftCabinet:
            newCabinet.append(i)
            stepcounter += 1

    if len(rightCabinet) > 0:
        for i in rightCabinet:
            newCabinet.append(i)
            stepcounter += 1
            
    return newCabinet

def mergesort(cabinet):
    
    if len(cabinet) == 1:
        return cabinet
    else:
        leftCabinet = mergesort(cabinet[:math.floor(len(cabinet) / 2)])
        rightCabinet = mergesort(cabinet[math.floor(len(cabinet) / 2):])
        return merging(leftCabinet, rightCabinet)
    
def check_steps(size_of_cabinet): # is used to count the number of steps it takes to sort a cabinet of a given size
    global stepcounter
    stepcounter = 0
    cabinet = [int(100 * random.random()) for i in range(size_of_cabinet)]
    mergesort(cabinet)
    return stepcounter


def plotSteps(): #main
    random.seed(8080) # sets the seed to 8080
    xs = list(range(1,100)) # creates a list of numbers from 1 to 100
    ys_mergesort = [check_steps(x) for x in xs] # creates a list of the number of steps it takes to sort a cabinet mergesort
    ys_exp = [math.exp(x) for x in xs] # creates a list of the exponential of the numbers in xs
    ys_squred = [x**2 for x in xs] # creates a list of the numbers in xs squared
    ys_threehalves = [x**(3/2) for x in xs] # creates a list of the numbers in xs to the power of 3/2
    #ys_cubed = [x**3 for x in xs] # creates a list of the numbers in xs cubed
    ys_nlogn = [x*math.log(x) for x in xs] # this is nlogn O(nlogn)
    ys_linear = [x for x in xs] # this is a linear function
    
    plt.plot(xs,ys_mergesort) # plots the number of steps it takes to sort a cabinet of a given size
    axes = plt.gca() # gets the current axes
    axes.set_ylim([np.min(ys_mergesort), np.max(ys_mergesort)+140]) # sets the y axis to the minimum of ys and the maximum of ys plus 140
    plt.plot(xs,ys_exp, label = 'exp') # plots the exponential of the numbers in xs
    
    plt.plot(xs,ys_linear, label = "linear")
    plt.plot(xs, ys_nlogn, label = "nlogn")
    plt.plot(xs,ys_mergesort, label = "merge sort") # plots the number of steps it takes to sort a cabinet of a given size
    plt.plot(xs,ys_squred, label = "squared") # plots the numbers in xs squared
    plt.plot(xs,ys_threehalves, label = "threehalves")  # plots the numbers in xs to the power of 3/2
    #plt.plot(xs,ys_cubed, label = "cubed") # plots the numbers in xs cubed
    plt.plot(xs,ys_exp, label = "exp") # plots the exponential of the numbers in xs
    plt.legend() # creates a legend
    
    plt.title("Steps Required for Each O")
    plt.xlabel("Number of elements")
    plt.ylabel("Steps Required to Sort")
    
    plt.show()




""" leftCabinet = [1, 3, 4, 4, 5, 7, 8, 9]
rightCabinet = [2, 4, 6, 7, 8, 8, 10, 12, 13, 14]
newCab = merging(leftCabinet, rightCabinet)
print(newCab)
print("Number of steps:", stepcounter)"""

def plot_steps_vs_size():
    sizes = list(range(1, 100))
    #sizes = [6,6,6,6]
    steps = [check_steps(n) for n in sizes]

    plt.plot(sizes, steps, marker='o')
    plt.title("Merge Sort Steps vs. Number of Elements")
    plt.xlabel("Number of Elements")
    plt.ylabel("Number of Steps")
    plt.show()

#plot_steps_vs_size()

plotSteps()