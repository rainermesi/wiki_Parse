import numpy as np
import random
# import regex module
import re
# import additional data structures module
# defaultdict is like a dictionary but returns a default value when called with a non-existent key
from collections import defaultdict

# Read text from file and tokenize.
path = 'pride-and-prejudice.txt'

# Alternative way to open/read the file
#temp_text = open(path,encoding='utf-8').read()

with open(path,encoding='utf-8') as f:
    text = f.read()

# list comprehension
# [expression for item in list if condition is met]

tokenized_text = [
    word
    for word in re.split('\W+', text)
    if word != ''
]


# Create graph.
# defaultdict inside a defaultdict?
markov_graph = defaultdict(lambda: defaultdict(int))

last_word = tokenized_text[0].lower()
for word in tokenized_text[1:]:
  word = word.lower()
  markov_graph[last_word][word] += 1
  last_word = word

# Preview graph.
limit = 3
for first_word in ('the', 'by', 'who'):
  next_words = list(markov_graph[first_word].keys())[:limit]
  for next_word in next_words:
    print(first_word, next_word)

# Generate sentences.
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
  #print('Weights 1: ',weights)
  # Normalize word counts to sum to 1.
  weights /= weights.sum()
  #print('Weights 2: ',weights)

  # Pick a destination using weighted distribution.
  choices = list(markov_graph[start_node].keys())
  chosen_word = np.random.choice(choices, None, p=weights)
  
  return [chosen_word] + walk_graph(
      graph, distance=distance-1,
      start_node=chosen_word)

walk_graph(markov_graph,start_node='most')
  
for i in range(10):
  print(' '.join(walk_graph(
      markov_graph, distance=12)), '\n')