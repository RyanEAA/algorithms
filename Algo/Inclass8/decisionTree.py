import csv
import numpy as np

file_path = "/Users/ryan/Desktop/Algo/Algo/Inclass8/variables.csv"

import pandas as pd
ess = pd.read_csv('./InClass8/ess.csv')


# print(ess.shape)
# print(ess.loc[:, 'happy'].head())
# print(ess.loc[:, 'sclmeet'].head())

# Fix typo in variable name

ess = ess.loc[ess['sclmeet'] <= 10,:].copy()
ess = ess.loc[ess['rlgdgr'] <= 10,:].copy()
ess = ess.loc[ess['hhmmb'] <= 50,:].copy()
ess = ess.loc[ess['netusoft'] <= 5,:].copy()
ess = ess.loc[ess['agea'] <= 200,:].copy()
ess = ess.loc[ess['health'] <= 5,:].copy()
ess = ess.loc[ess['happy'] <= 10,:].copy()
ess = ess.loc[ess['eduyrs'] <= 100,:].copy().reset_index(drop=True)

social = list(ess.loc[:, 'sclmeet'])
happy = list(ess.loc[:, 'happy'])
low_social_happiness = [hap for soc, hap in zip(social, happy) if soc <= 5]
high_social_happiness = [hap for soc, hap in zip(social, happy) if soc > 5]
meanlower = np.mean(low_social_happiness)
meanhigher = np.mean(high_social_happiness)
np.random.seed(518)
ess_shuffled = ess.reindex(np.random.permutation(ess.index)).reset_index(drop = True)
training_data = ess_shuffled.loc[0:37000,:]
test_data = ess_shuffled.loc[37001:,:].reset_index(drop = True)

print("mean happiness of high social is: ", meanhigher)
print("mean happiness of low social is: ", meanlower, "\n")

def get_splitpoint(allvalues, predictedvalues):
    lowest_error = float('inf')
    best_split = None
    for pctl in range(0, 100):
        split_candidate = np.percentile(allvalues, pctl)
        loweroutcomes = [outcome for value, outcome in zip(allvalues, predictedvalues) if value <= split_candidate]
        higheroutcomes = [outcome for value, outcome in zip(allvalues, predictedvalues) if value > split_candidate]
        if np.min([len(loweroutcomes), len(higheroutcomes)]) > 0:
            meanlow = np.mean(loweroutcomes)
            meanhigher = np.mean(higheroutcomes)
            # Fix typo in variable name
            lowererrors = [abs(outcome - meanlow) for outcome in loweroutcomes]
            highererrors = [abs(outcome - meanhigher) for outcome in higheroutcomes]
            total_error = sum(lowererrors) + sum(highererrors)
            if total_error < lowest_error:
                best_split = split_candidate
                lowest_error = total_error
    return best_split, lowest_error

allvalues = list(ess.loc[:, 'hhmmb'])
predictedvalues = list(ess.loc[:, 'happy'])

def getsplit(depth, data, variables, outcome_variable, maxdepth):
    best_var = ''
    lowest_error = float('inf')
    best_split = None
    best_lowermean = -1
    best_highermean = -1
    predictedvalues = list(data.loc[:, outcome_variable])
    for var in variables:
        allvalues = list(data.loc[:, var])
        split_candidate, error = get_splitpoint(allvalues, predictedvalues)
        if error < lowest_error:
            best_split = split_candidate
            lowest_error = error
            best_var = var
            best_lowermean = np.mean([outcome for value, outcome in zip(allvalues, predictedvalues) if value <= best_split])
            best_highermean = np.mean([outcome for value, outcome in zip(allvalues, predictedvalues) if value > best_split])
    generated_tree = [best_var, best_split, [], []]
    if depth < maxdepth:
        # Fix assignment to splitdata1 and splitdata2
        splitdata1 = data.loc[data[best_var] <= best_split, :]
        splitdata2 = data.loc[data[best_var] > best_split, :]
        if len(splitdata1.index) > 10 and len(splitdata2.index) > 10:
            generated_tree[2] = getsplit(depth + 1, splitdata1, variables, outcome_variable, maxdepth)
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
        variable_tocheck = tree[0]
        bound = tree[1]
        if observation[variable_tocheck] <= bound:
            tree = tree[2]
        else:
            tree = tree[3]
        if isinstance(tree, list):
            keepgoing = True
        else:
            keepgoing = False
            prediction = tree
    return prediction

variables = ['sclmeet','rlgdgr','hhmmb','netusoft','agea','eduyrs','health']
predictions=[]
outcome_variable = 'happy'
maxdepth = 4
thetree = getsplit(0,ess,variables,outcome_variable,maxdepth)

for k in range(0,30):
    observation = ess.loc[k,:]
    predictions.append(get_prediction(observation,thetree))
print("Predictions of our variables and the level of happiness:", predictions, "\n")

thetree = getsplit(0,training_data,variables,outcome_variable, maxdepth)

predictions = []
for k in range(0,len(test_data.index)):
    observation = test_data.loc[k,:]
    predictions.append(get_prediction(observation,thetree))
test_data.loc[:,'predicted'] = predictions
errors = abs(test_data.loc[:,'predicted'] - test_data.loc[:,'happy'])
print("Error rate of predicted minus happiness:", np.mean(errors))