import matplotlib.pyplot as plt

def ball_trajectory(v1, v2, x):
    location = v2*x/v1 - (9.81*(x**2)/(2*(v1**2)))
    return location

v1 = .99
v2 = 9.9
xs = [x/100 for x in list(range(201))]
ys = [ball_trajectory(v1,v2,x) for x in xs]

""" plt.plot(xs,ys)
plt.title('the trajectory of the thrown ball')
plt.xlabel('horizontal position of ball')
plt.ylabel('verttical position of ball')
plt.axhline('y = 0')
plt.show() """

#adding code
xs2 = [0.1, 2]
ys2 = [ball_trajectory(v1, v2, 0.1), 0]
xs3 = [0.2,2]
ys3 = [ball_trajectory(v1,v2,0.2),0]
xs4 = [0.3,2]
ys4 = [ball_trajectory(v1,v2,0.3),0]

plt.title('the trajectory of the thrown ball with lines of sight')
plt.xlabel('horizontal position of ball')
plt.ylabel('verttical position of ball')
plt.plot(xs,ys,xs2,ys2,xs3,ys3,xs4,ys4)
plt.show()

