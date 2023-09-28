import math

import matplotlib.pyplot as plt


def income(edu_years):
    return(math.sin((edu_years - 10.6)* (2*math.pi/4)) + (edu_years-11)/2) 

def EduIncomePlt(edu_years):
    xs = [11 + x/100 for x in list(range((901)))]
    ys = [income(x) for x in xs] 
    plt.plot(xs, ys)
    plt.plot(edu_years, income(edu_years), 'ro')
    plt.title('Education and Income')
    plt.xlabel('Years of Education')
    plt.ylabel('Lifetime Income')
    plt.show()
    
    
def income_derivative(edu_yrs):
    return(math.cos((edu_yrs - 10.6)* (2*math.pi/4)) * (2*math.pi/4) + 1/2)


current_edu = 12.5

EduIncomePlt(current_edu)
print("education/income derivatinve before maximizing: ", income_derivative(current_edu), "\n")

threshold = 0.0001
maximum_iterations = 100000
step_size = 0.001
iterations = 0

keep_going = True
while(keep_going):
    education_change = step_size * income_derivative(current_edu)
    current_edu = current_edu + education_change
    if(abs(education_change) < threshold):
        keep_going = False
        
    if(iterations >= maximum_iterations):
        keep_going = False
    iterations += 1

print("maximized number of years of education: ", current_edu, "\n")
EduIncomePlt(current_edu)
print("edication/income derivatinve after maximizin: ", income_derivative(current_edu), "\n")