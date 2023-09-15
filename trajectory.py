import matplotlib.pyplot as plt

#function has to be on top for program to run
def ball_trajectory(v1, v2, x):
    location = v2*x/v1 - (9.81*(x**2)/(2*(v1**2)))
    return location

#variables describing environment
v1 = .99
v2 = 9.9
xs = [x/100 for x in list(range(201))]
ys = [ball_trajectory(v1,v2,x) for x in xs]

#setting up the plot
plt.plot(xs,ys)
plt.title('the trajectory of the thrown ball')
plt.xlabel('horizontal position of ball')
plt.ylabel('verttical position of ball')
plt.axhline('y = 0')
plt.show()



