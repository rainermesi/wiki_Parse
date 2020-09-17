
#%%
import numpy as np
import random
# import regex module
import re
# import additional data structures module
# defaultdict is like a dictionary but returns a default value when called with a non-existent key
from collections import defaultdict

#%%
# nested tempdict to count the number of instances for each letter after the first letter
# defaultdict in defaultdict creates acts as a counter
# lambda is used because defaultdict needs an argument (not defaultdict) otherwise returns an error
tempdict = defaultdict(lambda:defaultdict(int))
# sample text
list_ow = 'mingi tekst mis vajab lahti löömist siin ei maksa pikalt peatuda sest peaminister ei ole adekvaatne meie vestluses osalema ta arvab et aguraijujaid pole olemas vaid need on väljamõeldised'.split()

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
      list(markov_graph[start_node].values()),
      dtype=np.float64)
  # Normalize word counts to sum to 1.
  weights /= weights.sum()

  # Pick a destination using weighted distribution.
  choices = list(markov_graph[start_node].keys())
  chosen_word = np.random.choice(choices, None, p=weights)
  
  return [chosen_word] + walk_graph(
      graph, distance=distance-1,
      start_node=chosen_word)
  
for i in range(10):
  print(' '.join(walk_graph(
      markov_graph, distance=12)), '\n')
