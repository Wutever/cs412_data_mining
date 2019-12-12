import pandas as pd
import numpy as np
import json



def user_case1(data, dic, col_name):
            
    for key, arr in dic.items():
        data = data[data[key].isin(arr)]
    
    value_counts = data[col_name].value_counts()
    
    ret1 = dict(zip(value_counts.index, value_counts.values))
    ret2 = dict(zip(value_counts.index, value_counts.values/len(data.index)))

    return ret1, ret2




def convert(o):
    if isinstance(o, np.int64): 
    	return int(o)  
    raise TypeError


def pieChart(dict, col, index):
    data = pd.read_csv(index)
    count, proportion = user_case1(data, dict,col)
    return json.dumps(count, default=convert)

