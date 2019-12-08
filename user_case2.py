import pandas as pd
import numpy as np
import json

data = pd.read_csv('hotel_cleaned.csv')

def convert(o):
    if isinstance(o, np.int64): 
    	return int(o)  
    raise TypeError



def user_case2(data, params, cols):
            
    for key, arr in params.items():
        data = data[data[key].isin(arr)]
    
    data = data.drop_duplicates(subset=['Hotel_Name']).sort_values(by=['Average_Score'], ascending=False)
    
    ret = [tuple(x) for x in data[cols].values]
    ret = json.dumps(ret, default=convert)

    return ret


ret = user_case2(data, {'Hotel_Country': ['United Kingdom'], 'Trip_Type': ['Leisure trip'], 'Traveler_Type': ['Couple'], 'Room_Type': ['Suite', 'Apartment'], 'Stay_Period': ['Stayed 3 nights']}, ['Hotel_Name', 'Hotel_Address', 'lat', 'lng', 'Average_Score'])

