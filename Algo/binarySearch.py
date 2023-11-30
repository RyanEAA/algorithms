import math
sortedCabinet = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

def binarySearch(cabinet, x): 
    upperBound = len(cabinet) - 1 #defines the length of cabinet
    lowerBound = 0 #defines the lower bound of the cabinet
    guess = math.floor(len(cabinet) / 2) #defines the guess as the middle of the cabinet
    
    while(abs(cabinet[guess] - x) != 0): #while the difference between the guess and the target is not 0
        if(cabinet[guess] > x): #if the guess is greater than the target
            upperBound = guess
            guess = math.floor((upperBound + lowerBound) / 2) #set the upper bound to the guess
            
        elif(cabinet[guess] < x): #if the guess is less than the target
            lowerBound = guess
            guess = math.floor((upperBound + lowerBound) / 2) #set the lower bound to the guess
            
    return guess

print("pos of 8: ", binarySearch(sortedCabinet, 8))
    
