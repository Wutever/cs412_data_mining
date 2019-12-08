import pandas as pd
import numpy as np
import json

data = pd.read_csv('hotel_cleaned.csv')


def user_case1(data, dic, col_name):
            
    for key, arr in dic.items():
        data = data[data[key].isin(arr)]
    
    value_counts = data[col_name].value_counts()
    
    ret1 = dict(zip(value_counts.index, value_counts.values))
    ret2 = dict(zip(value_counts.index, value_counts.values/len(data.index)))

    return ret1, ret2


count, proportion = user_case1(data, {'Trip_Type': ['Leisure trip'], 'Traveler_Type': ['Solo traveler', 'Couple']}, 'Stay_Period')

def convert(o):
    if isinstance(o, np.int64): 
    	return int(o)  
    raise TypeError

count = json.dumps(count, default=convert)
print(count)

proportion = json.dumps(proportion, default=convert)
print(proportion)
