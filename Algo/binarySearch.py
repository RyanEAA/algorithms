import math
sortedCabinet = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

def binarySearch(cabinet, x):
    upperBound = len(cabinet) - 1
    lowerBound = 0
    guess = math.floor(len(cabinet) / 2)
    
    while(abs(cabinet[guess] - x) != 0):
        if(cabinet[guess] > x):
            upperBound = guess
            guess = math.floor((upperBound + lowerBound) / 2)
            
        elif(cabinet[guess] < x):
            lowerBound = guess
            guess = math.floor((upperBound + lowerBound) / 2)   
            
    return guess

print("pos of 8: ", binarySearch(sortedCabinet, 8))
    
