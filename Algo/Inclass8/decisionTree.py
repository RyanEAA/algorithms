# Inclass Assignment-8 – COSC 2316 – Professor McCurry

#  Implemented by - Ryan Aparicio
import csv
import numpy as np

file_path = "/Users/ryan/Desktop/Algo/Algo/Inclass8/variables.csv"

import pandas as pd
ess = pd.read_csv('./InClass8/ess.csv')


# print(ess.shape)
# print(ess.loc[:, 'happy'].head())
# print(ess.loc[:, 'sclmeet'].head())

# Fix typo in variable name



ess = ess.loc[ess['sclmeet'] <= 10,:].copy() # copying the data 
ess = ess.loc[ess['rlgdgr'] <= 10,:].copy() 
ess = ess.loc[ess['hhmmb'] <= 50,:].copy() 
ess = ess.loc[ess['netusoft'] <= 5,:].copy()
ess = ess.loc[ess['agea'] <= 200,:].copy()
ess = ess.loc[ess['health'] <= 5,:].copy()
ess = ess.loc[ess['happy'] <= 10,:].copy()
ess = ess.loc[ess['eduyrs'] <= 100,:].copy().reset_index(drop=True)

social = list(ess.loc[:, 'sclmeet']) # creating a list of the social variable
happy = list(ess.loc[:, 'happy']) # creating a list of the happy variable
low_social_happiness = [hap for soc, hap in zip(social, happy) if soc <= 5] # creating a list of the low social happiness
high_social_happiness = [hap for soc, hap in zip(social, happy) if soc > 5] # creating a list of the high social happiness
meanlower = np.mean(low_social_happiness) # calculating the mean of the low social happiness
meanhigher = np.mean(high_social_happiness) # calculating the mean of the high social happiness
np.random.seed(518) # setting the seed
ess_shuffled = ess.reindex(np.random.permutation(ess.index)).reset_index(drop = True) # shuffling the data
training_data = ess_shuffled.loc[0:37000,:] # splitting the data
test_data = ess_shuffled.loc[37001:,:].reset_index(drop = True) # splitting the data

print("mean happiness of high social is: ", meanhigher) # printing the mean of the high social happiness
print("mean happiness of low social is: ", meanlower, "\n") # printing the mean of the low social happiness

def get_splitpoint(allvalues, predictedvalues): 
    lowest_error = float('inf')
    best_split = None
    for pctl in range(0, 100): # looping through the range of 0 to 100
        split_candidate = np.percentile(allvalues, pctl) # calculating the percentile
        
        # get the mean of the lower and higher outcomes
        loweroutcomes = [outcome for value, outcome in zip(allvalues, predictedvalues) if value <= split_candidate]
        
        # gets the mean higher outcomes
        higheroutcomes = [outcome for value, outcome in zip(allvalues, predictedvalues) if value > split_candidate]
        if np.min([len(loweroutcomes), len(higheroutcomes)]) > 0: # if the minimum of the lower and higher outcomes is greater than 0
            meanlow = np.mean(loweroutcomes)
            meanhigher = np.mean(higheroutcomes)
            
            
            # get the error of the lower and higher outcomes
            lowererrors = [abs(outcome - meanlow) for outcome in loweroutcomes]
            highererrors = [abs(outcome - meanhigher) for outcome in higheroutcomes]
            
            # get the total error
            total_error = sum(lowererrors) + sum(highererrors)
            if total_error < lowest_error:
                best_split = split_candidate
                lowest_error = total_error
    return best_split, lowest_error


#locates the data with 'hhmmb'
allvalues = list(ess.loc[:, 'hhmmb'])
predictedvalues = list(ess.loc[:, 'happy'])

def getsplit(depth, data, variables, outcome_variable, maxdepth):
    
    # Fix assignment to best_var, lowest_error, best_split, best_lowermean, best_highermean
    best_var = ''
    lowest_error = float('inf')
    best_split = None
    best_lowermean = -1
    best_highermean = -1
    
    # makes a list of data with the outcome variable
    predictedvalues = list(data.loc[:, outcome_variable])
    for var in variables:
        # for var in variables:
        allvalues = list(data.loc[:, var])
        split_candidate, error = get_splitpoint(allvalues, predictedvalues) # gets the split candidate and error
        if error < lowest_error:
            best_split = split_candidate
            lowest_error = error
            best_var = var
            
            # get the mean of the lower and higher outcomes
            best_lowermean = np.mean([outcome for value, outcome in zip(allvalues, predictedvalues) if value <= best_split])
            
            # gets the mean higher outcomes
            best_highermean = np.mean([outcome for value, outcome in zip(allvalues, predictedvalues) if value > best_split])
    generated_tree = [best_var, best_split, [], []]
    if depth < maxdepth:
        # Fix assignment to splitdata1 and splitdata2
        splitdata1 = data.loc[data[best_var] <= best_split, :] # splits the data
        splitdata2 = data.loc[data[best_var] > best_split, :] # splits the data
        if len(splitdata1.index) > 10 and len(splitdata2.index) > 10:
            generated_tree[2] = getsplit(depth + 1, splitdata1, variables, outcome_variable, maxdepth) # gets the split
            generated_tree[3] = getsplit(depth + 1, splitdata2, variables, outcome_variable, maxdepth) 
        else:
            depth = maxdepth + 1
            generated_tree[2] = best_lowermean
            generated_tree[3] = best_highermean
    else:
        generated_tree[2] = best_lowermean
        generated_tree[3] = best_highermean
    return generated_tree

def get_prediction(observation, tree):
    j = 0
    keepgoing = True
    prediction = -1
    while keepgoing:
        j = j + 1
        variable_tocheck = tree[0] # gets the variable to check
        bound = tree[1]
        if observation[variable_tocheck] <= bound:
            tree = tree[2]
        else:
            tree = tree[3]
        if isinstance(tree, list): # if the tree is a list
            keepgoing = True
        else:
            keepgoing = False # if the tree is not a list
            prediction = tree
    return prediction

variables = ['sclmeet','rlgdgr','hhmmb','netusoft','agea','eduyrs','health'] # creating a list of the variables
predictions=[] # creating a list of the predictions
outcome_variable = 'happy' # setting the outcome variable
maxdepth = 4 # setting the max depth 
thetree = getsplit(0,ess,variables,outcome_variable,maxdepth) # gets the split

for k in range(0,30): # looping through the range of 0 to 30
    observation = ess.loc[k,:] # gets the observation
    predictions.append(get_prediction(observation,thetree)) # appends the prediction
print("Predictions of our variables and the level of happiness:", predictions, "\n") # printing the predictions

thetree = getsplit(0,training_data,variables,outcome_variable, maxdepth)

predictions = []
for k in range(0,len(test_data.index)): # looping through the range of 0 to the length of the test data
    observation = test_data.loc[k,:] # gets the observation
    predictions.append(get_prediction(observation,thetree)) # appends the prediction
test_data.loc[:,'predicted'] = predictions # locates the predicted data
errors = abs(test_data.loc[:,'predicted'] - test_data.loc[:,'happy']) # calculates the errors
print("Error rate of predicted minus happiness:", np.mean(errors))