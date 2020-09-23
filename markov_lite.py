
#%%
import numpy as np
import pandas as pd
import random
# import regex module
import re
# import additional data structures module
# defaultdict is like a dictionary but returns a default value when called with a non-existent key
from collections import defaultdict
from collections import Counter

# %%
# read in corpus
wiki_txt = open(r'C:\Users\raine\Downloads\etwiki_latest\wiki_et.txt','r',encoding='utf-8').read()
list_ow = wiki_txt.lower().split()

# list_ow = open('test_corpus.txt',"r",encoding='utf-8').read().upper().split()
# %%
# get word lenght weights in corpus

def word_len_df_gen(in_list):
    count_list = [len(item) for item in in_list]
    count_df = pd.DataFrame.from_dict(collections.Counter(count_list).items())
    count_df[2] = count_df[1] / count_df[1].sum()
    return count_df

word_len_df = word_len_df_gen(list_ow)

def rand_word_len_picker(in_df):
    return np.random.choice(in_df[0],p=in_df[2])

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
# check results & clean up foreign letters
# estonian alphabet
abc = ['A', 'a', 'B', 'b', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'R', 'r', 'S', 's', 'Š', 'š', 'Z', 'z', 'Ž', 'ž', 'T', 't', 'U', 'u', 'V', 'v', 'Õ', 'õ', 'Ä', 'ä', 'Ö', 'ö', 'Ü', 'ü']
abc = list(dict.fromkeys(i.lower() for i in abc))

# 2 approaches here:
# clean primary keys
tempdict2 = dict((k, tempdict[k]) for k in abc 
                                         if k in tempdict) 
# clean nested key value pairs
for letter in abc:
  for item in tempdict2[letter].copy():
    if item not in abc:
      del tempdict2[letter][item]

# %%
tempdict = tempdict2
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

# distance > lenght of word

def walk_graph(graph, distance=3, start_node=None):
  """Returns a list of words from a randomly weighted walk."""
  if distance <= 0:
    return []
  
  # If not given, pick a start node at random.
  if not start_node:
    start_node = random.choice(list(graph.keys()))
  
  
  weights = np.array(
      list(graph[start_node].values()),
      dtype=np.float64)
  # Normalize letter counts to sum to 1. Create % weights for each letter.
  weights /= weights.sum()

  # Pick next letter using weighted distribution.
  choices = list(graph[start_node].keys())
  chosen_letter = np.random.choice(choices, None, p=weights)
  
  # recursively build a word until distance = 0
  return [chosen_letter] + walk_graph(
      graph, distance=distance-1,
      start_node=chosen_letter)
# %%

# print out a list of generated words
# join the list of letters the function produces '' is the joining character
# '\n' is adds a newline between prints

word_file = open('word_file.txt','a',encoding='utf-8')

for i in range(1000): 
  word_file.write(''.join(walk_graph(tempdict,rand_word_len_picker(word_len_df))))
  word_file.write('\n')

word_file.close()

# %%
# make a graph

viz_df = pd.DataFrame.from_dict(tempdict)
viz_df = viz_df.stack().reset_index()
viz_df.columns = ['p_letter','s_letter','l_count']

# %%
viz_df['l_rank'] = viz_df.groupby('p_letter')['l_count'].rank('dense',ascending=False)

# %%
viz_df.to_csv('viz_df.csv')

# %%
# notes:

# --next steps--

# $ add wiki corpus
# $ create a weighed list of word lenghts in corpus. Use the list to generate new words with random lenghts
# $ remove non alphabetic characters from corpus
# $ what other stats can I get out of the corpus? Avg word lengts, popular words, least popular words?

# --random module--

# random. offers different random object gerators
# choice generates random objects from a list
#
# random.choice([1,2,3,4,5])
# random.choice(list(tempdict.keys()))

# --np.array, normalizing counts and % weights--

# np.array creates an array with dictionary item values that can be manipulated. In this case letter counts.
# /= divides the variable with itself
# .sum ads up all the vallues in the np.array
# dividing each array element by the sum of the array gives the percentage weight of the element to the whole
# It is the same things as :
# (np.array([1,2,3,4,5]) / np.array([1,2,3,4,5]).sum())
#
# weights = np.array(list(tempdict['m'].values()),dtype=np.float64) / np.array(list(tempdict['m'].values()),dtype=np.float64).sum()
# weights /= weights.sum()

# --weighed choices--

# this is combined into making random but weighed choices
# np.random.choice([1,2,3,4,5], None, p=(np.array([1,2,3,4,5]) / np.array([1,2,3,4,5]).sum()))

# %%
