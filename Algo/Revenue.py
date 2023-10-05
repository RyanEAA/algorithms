# Inclass Assignment-3 – COSC 2316 – Professor McCurry

#  Implemented by - Brandon Dove


import math
import matplotlib.pyplot as plt


# our function for calculating the tax rates on a graph

def revenue(tax):
    return (100 * ( math.log ( tax + 1 ) - ( tax - .2 ) ** 2 + .04 ))


# our function that is plotting our graph, labeling it, and putting our tax function on the graph.

def taxPlot(tax):
    xs = [x/1000 for x in range(1001)]
    ys = [revenue_flipped(x) for x in xs]
    plt.plot(xs,ys)
    plt.title('Tax / Revenue Flipped')
    plt.xlabel('Tax Rate')
    plt.ylabel('Revenue - Flipped')
    plt.plot(tax, revenue_flipped(tax), 'ro')
    plt.show()
    

# functions that handles our slope of our tax curve, calculates derivatives and inverse derivatives

def revenue_derivative(tax):
    return 100 * (1 / (tax + 1) - 2 * (tax - 0.2))


def revenue_derivative_flipped(tax):
    return(0 - revenue_derivative(tax))


def revenue_flipped(tax):
    return(0 - revenue(tax))



# function that calculates the min revenue we can achieve, gives us the best rate.

def min_revenue(step_size, threshold, max_iterations, iterations, current_rate):
    keep_going = True
    while(keep_going):
        rate_change = step_size * revenue_derivative_flipped(current_rate)
        current_rate = current_rate - rate_change
        if (abs(rate_change) < threshold):
            keep_going = False
        if (iterations >= max_iterations):
            keep_going = False
        iterations = iterations + 1
    return current_rate
            



def main():
    current_rate = .7
    taxPlot(current_rate)
        
    # shows our current position on our equation, as well with current revenue
    
    print("The current revenue is: ", revenue(current_rate), "\n")

    # shows our current rate, as well if revenue increases or decreases, and what the slope of the line is.
    
    print("The revenue derivative of the current rate is: ", revenue_derivative(current_rate), "\n")
    
    
    print("Flipped revenue derivative before minimizing: ", revenue_derivative(current_rate), "\n")
    
    step_size = 0.001
    threshold = 0.0001
    max_iterations = 100000
    iterations = 0
    
    min_rate = min_revenue(step_size, threshold, max_iterations, iterations, current_rate)  
    
    taxPlot(min_rate)
    
    print("Flipped revenue derivative after minimizing: ", revenue_derivative_flipped(min_rate), "\n")
    
    revenue_derivative(min_rate)
    
    print("Minimized tax rate: ", min_rate)
    
    
   

    
    
    

if __name__ == "__main__":
    main()
    
    # main method call to run our outputs.