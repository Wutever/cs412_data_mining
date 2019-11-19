import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import json

def dbscan(df, categorical_dict, numeric_columns, eps, minpts):
    """ 
    DBSCAN.
  
    Parameters: 
    df (pandas dataframe)
    categorical_dict (dict): dictionary of user-defined categorical values
    numeric_columns (list): list of numerical columns for clustering
    eps (int)
    minpts (int)

    Returns:
    labels (list): labels for the cluster the location is in
    count (list): count of number of application records at each location
    """
    
    if categorical_dict:
        for key, arr in categorical_dict.items():
            for value in arr:
                df = df[df[key] == value]
        
    df['new'] = list(zip(df[numeric_columns[0]], df[numeric_columns[1]]))
    value_counts = df['new'].value_counts()
    data = list(value_counts.index)
    labels = [0]*len(data)
    num = 0
    
    for i in range(0, len(data)):
        if labels[i] != 0:
            continue
            
        neighbors = []
        for j in range(0, len(data)):
            if np.linalg.norm([np.array(data[i])-np.array(data[j])]) < eps:
                neighbors.append(j)
            
        if len(neighbors) < minpts:
            labels[i] = -1
        else:
            num += 1
            labels[i] = num
            j = 0
            while j < len(neighbors):
                if labels[neighbors[j]] == -1:
                    labels[neighbors[j]] = num
                elif labels[neighbors[j]] == 0:
                    labels[neighbors[j]] = num
                    
                    new_neighbors = []
                    for k in range(0, len(data)):
                        if np.linalg.norm([np.array(data[neighbors[j]])-np.array(data[k])]) < eps:
                            new_neighbors.append(k)
                            
                    if len(new_neighbors) >= minpts:
                        neighbors = neighbors + new_neighbors
                j += 1        
    
    labels = list(labels)
    count = list(value_counts.values)
    
    return labels, count

df = pd.read_csv('h1b_kaggle.csv', na_values = 'NaN')
df = df.drop(columns = ['Unnamed: 0'])
df = df.dropna()



def convert(o):
    if isinstance(o, np.int64): 
    	return int(o)  
    raise TypeError

def dbscan1(dict):
    labels, count = dbscan(df, dict, ['lon', 'lat'], 2, 10)
    labels = json.dumps(labels, default=convert)
    print(labels)

    count = json.dumps(count, default=convert)
    print(count)

