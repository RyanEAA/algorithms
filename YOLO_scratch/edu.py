# Inclass Assignment-4 – COSC 2316 – Professor McCurry

#  Implemented by - Ryan Aparicio


#imports math
import math

#import matplotlib
import matplotlib.pyplot as plt


#function of income
def income(edu_years):
    return(math.sin((edu_years - 10.6)* (2*math.pi/4)) + (edu_years-11)/2) 


#function of income plot
def EduIncomePlt(edu_years):
    xs = [11 + x/100 for x in list(range((901)))]
    ys = [income(x) for x in xs] 
    plt.plot(xs, ys)
    plt.plot(edu_years, income(edu_years), 'ro')
    plt.title('Education and Income')
    plt.xlabel('Years of Education')
    plt.ylabel('Lifetime Income')
    plt.show()
    
    
#function of income derivative
def income_derivative(edu_yrs):
    return(math.cos((edu_yrs - 10.6)* (2*math.pi/4)) * (2*math.pi/4) + 1/2)

#trial 1
#current_edu = 12.5

#trial 2
#current_edu = 20

#trial 3
#current_edu = 25

#trial 4
current_edu = 15



#function calls
EduIncomePlt(current_edu)
print("education/income derivatinve before maximizing: ", income_derivative(current_edu), "\n")

#maximizing education
threshold = 0.0001
maximum_iterations = 100000
step_size = 0.001
iterations = 0

#while loop
keep_going = True
#while loop
while(keep_going):
    #if statement
    education_change = step_size * income_derivative(current_edu)
    
    
    current_edu = current_edu + education_change
    
    #if abs education change is less than threshold
    if(abs(education_change) < threshold):
        keep_going = False
    
    #if iterations is greater than or equal to maximum iterations
    if(iterations >= maximum_iterations):
        keep_going = False
    iterations += 1

print("maximized number of years of education: ", current_edu, "\n")

EduIncomePlt(current_edu)
print("edication/income derivatinve after maximizin: ", income_derivative(current_edu), "\n")




