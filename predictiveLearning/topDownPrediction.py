import numpy as np

np.random.seed(1)

def check_score(truth, guess):
    return np.sum(truth == guess)

numberOfQuestions = 16

pattern = np.random.choice([True, False], numberOfQuestions)

"""
Top Down Approach
"""

trials = []
for i in range(100):
    pat = np.random.choice([1.0, 0.0], numberOfQuestions)
    xs = []
    ys = []
    current_belief = np.zeros(numberOfQuestions)
    #initial check score to estimate the total number of trues and falses
    
    score = check_score(pat, current_belief)
    trial = 1
    total_zeros = score
    total_ones = numberOfQuestions-total_zeros
    xs.append(current_belief.copy())
    xs.append(1-current_belief.copy())
    ys.append(total_zeros)
    ys.append(total_ones)
    
    
    
    