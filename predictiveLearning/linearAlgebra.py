import numpy as np

np.random.seed(1)

def check_score(truth, guess):
    return np.sum(truth == guess)

numberOfQuestions = 16

pattern = np.random.choice([True, False], numberOfQuestions)

"""
Linear Algebra Method
"""
from scipy.optimize import lsq_linear

M = 16 # number of questions
#converts 1 to true and 0 to false


pat = np.zeros(M)
pat[pattern==True]  = 1.0
pat[pattern==False] = 0.0


xs = 1-np.eye(M) #generates 16 possible guesses
ys = np.zeros((M)) 
for i in range(len(ys)): #computes score for each guess
    ys[i] = check_score(pat, xs[i])
    
#linear solution with lower bound = 0 (F) and upper bound = 1 (T)
res = lsq_linear(xs, ys, bounds=(0,1))
ws = np.round(res.x)
score = check_score(pat, ws)
assert(score == M)
print("scored:", score)
print("Truth:", pat)
print("Guess:", ws)