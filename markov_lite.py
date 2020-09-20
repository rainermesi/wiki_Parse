
#%%
import numpy as np
import random
# import regex module
import re
# import additional data structures module
# defaultdict is like a dictionary but returns a default value when called with a non-existent key
from collections import defaultdict

# %%
# read in corpus
list_ow = open('test_corpus.txt',"r",encoding='utf-8').read().split()

#%%
# nested tempdict to count the number of instances for each letter after the first letter
# defaultdict in defaultdict creates acts as a counter
# lambda is used because defaultdict needs an argument (not defaultdict) otherwise returns an error
tempdict = defaultdict(lambda:defaultdict(int))

# parse sample text and count letters
# loop over words in list, save first words first letter
# start looping over letters in each word, staring from 2nd letter
# add first letter variable into dictiorary, add a nested key equal to loopin letter, increase counter by 1
# change first letter variable to second letter and restart loop
# this creates a dictionary with letters in the text, each letter has a nested dictionary of letters that followed it including count of occurances
for item in list_ow:
  item_prev_letter = item[0]
  for i in item[1:]:
    tempdict[item_prev_letter][i] += 1
    item_prev_letter = i

#%%
# check results
tempdict

#%%
# try to combine letters
# create a list of letters from above dictionary using the looping letter
# use .keys to slice the nested key list with letter_limit variable
# loop over the new list and concatenate primary looping letter with secondary looping letter
letter_limit = 3
for first_letter in ('u','a','e'):
  next_letters = list(tempdict[first_letter].keys())[:letter_limit]
  print(list(tempdict[first_letter].keys())[:letter_limit])
  for next_letter in next_letters:
    print(first_letter+next_letter)

# %%
# use numpy random choice
# undestand the final part

# distance > lenght of word

def walk_graph(graph, distance=5, start_node=None):
  """Returns a list of words from a randomly weighted walk."""
  if distance <= 0:
    return []
  
  # If not given, pick a start node at random.
  if not start_node:
    start_node = random.choice(list(graph.keys()))
  
  
  weights = np.array(
      list(tempdict[start_node].values()),
      dtype=np.float64)
  # Normalize word counts to sum to 1.
  weights /= weights.sum()

  # Pick a destination using weighted distribution.
  choices = list(tempdict[start_node].keys())
  chosen_word = np.random.choice(choices, None, p=weights)
  
  return [chosen_word] + walk_graph(
      graph, distance=distance-1,
      start_node=chosen_word)
  
for i in range(10):
  print(' '.join(walk_graph(
      tempdict, distance=5)), '\n')



# %%

# random. offers different random object gerators
# choice generates random objects from a list
#
# random.choice([1,2,3,4,5])
# random.choice(list(tempdict.keys()))

#

# np.array creates an array with dictionary item values that can be manipulated. In this case letter counts.
# /= divides the variable with itself
# .sum ads up all the vallues in the np.array
# dividing each array element by the sum of the array gives the percentage weight of the element to the whole
# It is the same things as :
# (np.array([1,2,3,4,5]) / np.array([1,2,3,4,5]).sum())
#
# weights = np.array(list(tempdict['m'].values()),dtype=np.float64) / np.array(list(tempdict['m'].values()),dtype=np.float64).sum()
# weights /= weights.sum()

#

# this is combined into making random but weighed choices
# np.random.choice([1,2,3,4,5], None, p=(np.array([1,2,3,4,5]) / np.array([1,2,3,4,5]).sum()))

#

# the last part is recursion?

# def factorial(x):
#   if x == 1:
#     return 1
#   else:
#     return (x * factorial(x-1))

# factorial(3)

# %%

start_node = random.choice(list(tempdict.keys()))

weights = np.array(
    list(tempdict[start_node].values()),
    dtype=np.float64)
# Normalize word counts to sum to 1.
weights /= weights.sum()

choices = list(tempdict[start_node].keys())

print('Start node: ',start_node, ' Weights: ', weights, 'Choices: ', choices)

np.random.choice(choices, None, p=weights)

# %%
