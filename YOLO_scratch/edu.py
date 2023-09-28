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
current_edu = 12.5
EduIncomePlt(current_edu)