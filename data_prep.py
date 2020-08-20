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
    u_df_et = u_df_et.groupby(['0','1']).sum()
    return u_df_et    
    
et_filter(u_df).to_csv('f_output.csv')