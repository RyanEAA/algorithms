import numpy as np

np.random.seed(1)

def check_score(truth, guess):
    return np.sum(truth == guess)

pattern = np.random.choice([True, False], 16)

"""
brute force method
"""
score = 0
trial = 0
while(True):
    guess = np.random.choice([True, False], 16)
    score = check_score(pattern, guess)
    if(score == 16):
        break
    trial += 1
print("scored:", score, "in", trial, "trials")