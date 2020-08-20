import xml.etree.ElementTree as ET

tree = ET.parse(r'C:\Users\raine\Downloads\etwiki-20200801-pages-meta-current.xml\etwiki-20200801-pages-meta-current.xml')
root = tree.getroot()

root.tag
root.attrib

for child in root:
    for gchild in child:
        print('tags: ', gchild.tag, 'attribs: ', gchild.attrib)

for child in root:
    for gchild in child.iter('revision'):
        print(gchild.attrib)

for child in root.findall('http://www.mediawiki.org/xml/export-0.10/'):
    print(child.attrib)

for child in root:
    for gchild in child:
        for revision in gchild.findall('revision'):
            print(revision.tag, revision.attrib)

for child in root:
    for gchild in child:
        if gchild.attrib is not None:
            for ggchild in gchild:
                if ggchild.tag == '{http://www.mediawiki.org/xml/export-0.10/}text':
                    print(ggchild.attrib)
                
#            pass
#        else:
#            print('tags: ', gchild.tag, 'attribs: ', gchild.attrib)

count = 1

for node in tree.iter('text'):
    while count < 6:
        print(node)
        count = count + 1

for node in tree.iter('text'):
    print(node.attrib)

print(count)

text_01 = ET.tostring(tree.getroot(),encoding='utf-8',method='text')

text_01.write(open('output.txt', 'wb'))

import math
import numpy as np
import pandas as pd
import plotly.express as px

string = 'See on esimene lause. See on teine lause. Siin on vaja rohkem kui kolme lauset. Üks lause peab veel olema.'
str_list = string.split()

str_list_pairs = []

for item in str_list:
    print(item[1])

for item in str_list:
    #print(item,len(item),len(item)/2,math.floor(len(item)/2))
    n_splits = math.floor(len(item)/2)
    split_index = 0
    slice_index = 0
    while split_index <= n_splits:
        try:
            str_list_pairs.append([item[slice_index],item[slice_index + 1]])
        except Exception:
            pass
        #try:
        #    str_list_pairs.append(item[slice_index + 1])
        #except Exception:
        #    pass
        slice_index = slice_index + 2
        split_index = split_index + 1

print(str_list_pairs)

str_df_pairs = pd.DataFrame(str_list_pairs)

str_df_pairs

str_df_pairs_bin = str_df_pairs

str_df_pairs_bin[2] = 1

str_df_pairs_bin

pd.pivot_table(str_df_pairs_bin,index=[0,1],values=[2],aggfunc='count')

str_df_pairs[str_df_pairs[0] == 'e']

def my_func(x):
    str_list = x.split()
    str_list_pairs = []
    for item in str_list:
        n_splits = math.floor(len(item)/2)
        split_index = 0
        slice_index = 0
        while split_index <= n_splits:
            try:
                str_list_pairs.append([item[slice_index],item[slice_index + 1]])
            except Exception:
                pass
            slice_index = slice_index + 2
            split_index = split_index + 1
    str_df_pairs = pd.DataFrame(str_list_pairs)
    str_df_pairs[2] = 1
    return pd.pivot_table(str_df_pairs,index=[0,1],values=[2],aggfunc='count')

my_func(string).to_csv('output.csv')

test_txt = open(r'C:\Users\raine\Downloads\etwiki_latest\wiki_et.txt','r',encoding='utf-8')

print(test_txt.readline())

abc = ['A', 'a', 'B', 'b', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'R', 'r', 'S', 's', 'Š', 'š', 'Z', 'z', 'Ž', 'ž', 'T', 't', 'U', 'u', 'V', 'v', 'Õ', 'õ', 'Ä', 'ä', 'Ö', 'ö', 'Ü', 'ü']
testdf = pd.read_csv('output.csv')

testdf = testdf[testdf['0'].isin(abc)]

testdf

import pandas as pd
import plotly.express as px

