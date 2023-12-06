import numpy as np

np.random.seed(1)

def check_score(truth, guess):
    return np.sum(truth == guess)


#generate a true and false pattern to simulate questions(randomly distributed)
pattern = np.random.choice([True, False], 16)

print(pattern)
