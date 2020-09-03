import numpy as np
import random
# import regex module
import re
# import additional data structures module
# defaultdict is like a dictionary but returns a default value when called with a non-existent key
from collections import defaultdict

# nested tempdict to count the number of instances for each letter after the first letter
tempdict = defaultdict(lambda:defaultdict(int))
# sample text
list_ow = 'mingi tekst mis vajab lahti löömist siin ei maksa pikalt peatuda sest peaminister ei ole adekvaatne meie vestluses osalema ta arvab et aguraijujaid pole olemas vaid need on väljamõeldised'.split()

# parse sample text and count letters
for item in list_ow:
  item_prev_letter = item[0]
  for i in item[1:]:
    tempdict[item_prev_letter][i] += 1
    item_prev_letter = i

# check results
tempdict

# try to combine letters
letter_limit = 3
for first_letter in ('u','a','e'):
  next_letters = list(tempdict[first_letter].keys())[:letter_limit]
  for next_letter in next_letters:
    print(first_letter+next_letter)

# use numpy random choice
# undestand the final part