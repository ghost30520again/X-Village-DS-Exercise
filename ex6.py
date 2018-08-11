import json
import requests

ptt = 'https://raw.githubusercontent.com/x-village/data-structure-course/master/external_data/ptt_0726_s.json'
        
datas = requests.get(ptt)
file = datas.json()

obj =[ ]
list_all = [ ]

for i in range(len(file)):
    
    x = file[i]['h_推文總數']
    if len(x) != 0:
        list_all.append(x['all'])
        obj.append(i)

        
index = sorted(set(list_all),reverse = True)

for i in range(len(index)):
    for j in obj:      
        k = file[j]['h_推文總數']['all']
        if k == index[i]:
            
            print('推文總數 = %d' % index[i])                        
            print(" ")
            