import math
import pandas as pd

# remove commas and punctuation from source string
# all lowercase source string

string = ('Uuest õppeaastast algab kõik Eesti koolides tavapäraselt, kuid näiteks tehakse 1. septembri aktuseid väiksemale rahvahulgale korraga ning nakkusjuhtumi ilmnemisel läheb terve klass kaugõppele, selgitas haridus- ja teadusminister Mailis Reps. Reps ütles kolmapäevasel kooliaasta algust tutvustaval pressikonverentsil, et karantiiniperioodil õnneks hariduse sisu ei kannatanud, kuid paljudes koolides tuleb siiski kevadel läbivõetud teemasid korrata. "Kooliaasta alguse sõnum on see, et sellist üldist vajadus digiõppega jätkata kuidagi ei ole. Meie numbrid on vägagi positiivsed, oleme koroonanakkuse suutnud hoida kontrolli all, aga ta ei ole ühiskonnast kuhugi kadunud," ütles Reps. Minister lisas, et lähenemine sügisel on kooli- ja piirkonnapõhine ning potentsiaalsetele koroonajuhtumitele lähenetakse lokaalselt. Kohalik kriisikomisjon koguneb Repsi sõnul siis, kui ligikaudu 10 protsenti ühe kooli õpilastest on viiruspositiivsed. Minister täpsustas, et number on umbkaudne, sest näiteks 20 õpilasega koolis on olukord teine. "Tuletame ka meelde, et nii nagu me leppisime kevadel kokku, sügisperioodil toimuvad lisagümnaasiumieksamid ja nendeks on registreerunud üsna palju õpilasi," sõnas Reps. Lisaks pööratakse tähelepanu digiõpikutele ja sellele, et õpetajatel ei tekiks liialt suurt koormust, kui nad peavad mõnel juhul andma nii kontakttunde kui ka e-tunde, sõnas Reps. Minister lisas, et koolidel ja lasteasutustel on õigus haiged lapsed koju saata ning regulaarselt laste kehatemperatuuri mõõta. Ühe ideena käis minister välja ka tunniplaanide osalise muutmise, näiteks algavad erinevate klassikomplektide tunnid erineval ajal, et koolimajas tekiks suurem hajutatus.')

wiki_txt = open(r'C:\Users\raine\Downloads\etwiki_latest\wiki_et.txt','r',encoding='utf-8').read()
wiki_txt_split = wiki_txt.split()

#wiki_txt_split_1 = wiki_txt.split()[:10000000]
#wiki_txt_split_2 = wiki_txt.split()[10000000:20000000]
#wiki_txt_split_3 = wiki_txt.split()[20000000:30000000]
#wiki_txt_split_4 = wiki_txt.split()[30000000:40000000]

isinstance(wiki_txt_split,list)

def my_func(x):
    #str_list = x.split()
    #str_list = str_list[:100]
    str_list = x
    str_list_pairs = []
    counter = 0
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
        print(counter)
        counter = counter + 1
    str_df_pairs = pd.DataFrame(str_list_pairs)
    str_df_pairs[2] = 1
    return pd.pivot_table(str_df_pairs,index=[0,1],values=[2],aggfunc='count')

my_func(wiki_txt_split).to_csv('output_2.csv')