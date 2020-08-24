import pandas as pd

def union_func(x,y):
    for i in range(x,y):
        #print(i
        if i == 1:
            temp_df = pd.read_csv('output_{}.csv'.format(i))
        elif i >= 2:
            temp_df = pd.concat([temp_df,pd.read_csv('output_{}.csv'.format(i))])
    return temp_df

u_df = union_func(1,11)

def et_filter(x):
    abc = ['A', 'a', 'B', 'b', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'R', 'r', 'S', 's', 'Š', 'š', 'Z', 'z', 'Ž', 'ž', 'T', 't', 'U', 'u', 'V', 'v', 'Õ', 'õ', 'Ä', 'ä', 'Ö', 'ö', 'Ü', 'ü']
    u_df_et = x[x['0'].isin(abc)]
    u_df_et = u_df_et[u_df_et['1'].isin(abc)]
    u_df_et = u_df_et.groupby(['0','1'],as_index=False).sum()
    u_df_et['3'] = u_df_et.groupby(['0'])['2'].rank(method='dense', ascending=False).astype(int)
    return u_df_et    
    
et_filter(u_df).to_csv('f_output.csv')

f_df = et_filter(u_df)
f_df
f_df['0']
f_df.loc[(f_df['0'] == 'h') & (f_df['3'] == 1)]['1'].values[0]

def walk_the_path(dataset,x,z):
    #dataset = dataset
    #x = starting letter
    #y = length of word
    word_list = []
    word_list.append(x)
    next_letter = dataset.loc[(dataset['0'] == x) & (dataset['3'] == 1)]['1'].values[0]
    word_list.append(next_letter)
    for i in range(z):
        fluid_letter = dataset.loc[(dataset['0'] == next_letter) & (dataset['3'] == 1)]['1'].values[0]
        word_list.append(fluid_letter)
        next_letter = fluid_letter
    #add first letter to list x
    #pick first sub-letter of x and add it to list
    #pick last element of list and find matching letter
    #pick first sub letter of last element and add it to list
    #repeat last 2 steps
    #check if list lenght = y, if true stop.
    return word_list

for i in f_df['0'].unique():
    #print(i)
    print(walk_the_path(f_df,i,6))