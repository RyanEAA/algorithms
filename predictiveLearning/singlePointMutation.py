import numpy as np

np.random.seed(1)

def check_score(truth, guess):
    return np.sum(truth == guess)

numberOfQuestions = 16

pattern = np.random.choice([True, False], numberOfQuestions)

"""
single point mutation
"""
guess = [False]*len(pattern) #initialize guess of all being false
score = check_score(pattern, guess) #check score of guess
trial = 1 #initialize trial counter

for i in range(len(guess)):
    guess[i] = True #toggles 1 element to true
    new_score = check_score(pattern, guess) #check score of new guess
    if(new_score < score):
        guess[i] = False #if new score is lower, toggle back to false
    else:
        score = new_score
    if(score == numberOfQuestions):
        break
    trial += 1
    
    
print("scored:", score, "in", trial, "trials")