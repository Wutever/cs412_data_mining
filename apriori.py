import numpy as np
import pandas as pd
import itertools
import pprint
pp = pprint.PrettyPrinter(width = 200)
import json

def apriori(data, threshold, length, columns = None):
    
    if columns != None:
        data = data[columns]
    #if length > len(data.columns)+1:
    #    raise ValueError('Desired length of itemsets must be smaller or equal to number of attributes.')
    if length > len(data.columns):
    	length = len(data.columns)
        
    data, itemsets, attributes, candidates = apriori_1(data, threshold)
    json_dict[1] = itemsets
    for n in range(2, length):
        data, itemsets, attributes, candidates, itemsets_with_support = apriori_n(data, itemsets, attributes, candidates, threshold, n)
        #print('length-' + str(n) + ' itemsets:')
        #print(' ')
        #pp.pprint(itemsets_with_support)
        #print(' ')
        #print(' ')

        for col_name, attr_dict in itemsets_with_support.items():
        	temp_attr = {}
        	for key, count in attr_dict.items():
        		temp_attr[str(key)] = count
        		itemsets_with_support[col_name] = temp_attr

        temp_dict = {}
        for key, value in itemsets_with_support.items():
            temp_dict[str(key)] = value
        json_dict[n] = temp_dict

    return data, itemsets, attributes, candidates, itemsets_with_support

        
def apriori_1(data, threshold):
    
    itemsets = {}
    for i in range(len(data.columns)):
        column = data.iloc[:, i]
        values = column.unique()
        frequent = column.value_counts()[column.value_counts() / n_rows > threshold]
        indices = list(frequent.index)
        values = list(frequent.values)
        items = dict(zip(indices, values))
        name = frequent.name
        itemsets[name] = items
        
    attributes = {}
    for key, value in itemsets.items():
        attributes[key] = set(value)
        
    reverse = {}
    for key, value in itemsets.items():
        for item in value:
            reverse[item] = key
        
    candidates = set([])
    for single_comb in list(itertools.combinations(attributes.keys(), 2)):
        
        list_list = []
        for col in list(single_comb):
            list_list.append(list(attributes[col]))
            
        for one in list(itertools.product(*list_list)):
            check = one
            flag = 0
            for i in check:
                if i not in reverse:
                    flag = 1
                    break
            if flag == 0:
                candidates.add(one)
        
    return data, itemsets, attributes, candidates


def apriori_n(data, length_nminus1_itemsets, attribute_list, length_n_candidates, threshold, n):

    for key, value in attribute_list.items():
        data = data[data[key].isin(value)]
        
    itemsets = {}
    for item in list(itertools.combinations(attribute_list.keys(), n)):
        if 'CASE_STATUS' in item:
            continue
        frequent = []
        grouped = data.groupby(list(item)).count().iloc[:,0] / n_rows > threshold
        for index in grouped[grouped[grouped.index] == True].index:
            frequent.append(index)
        itemsets[item] = frequent
        
    itemsets_with_support = {}
    for item in list(itertools.combinations(attribute_list.keys(), n)):
        if 'CASE_STATUS' in item:
            continue
        frequent = data.groupby(list(item)).count().iloc[:,0]
        grouped = frequent / n_rows > threshold
        frequent = frequent[grouped]
        indices = list(frequent.index)
        values = list(frequent.values)
        items = dict(zip(indices, values))
        itemsets_with_support[item] = items    
    
    attributes = {}
    for key, arr in itemsets.items():
        for k in key:
            if k not in attributes:
                attributes[k] = set([])
        for k in key:
            for value in arr:
                for i in range(len(value)):
                    attributes[key[i]].add(value[i])
                    attributes[key[i]].add(value[i])
                    
    reverse = {}
    for key, value in itemsets.items():
        for item in value:
            reverse[item] = key
            
    candidates = set([])
    for single_comb in list(itertools.combinations(attribute_list.keys(), n+1)):
        
        list_list = []
        for col in list(single_comb):
            list_list.append(list(attribute_list[col]))
            
        for one in list(itertools.product(*list_list)):
            check = list(itertools.combinations(list(one), n))
            flag = 0
            for i in check:
                if i not in reverse:
                    flag = 1
                    break
            if flag == 0:
                candidates.add(one)
    
    return data, itemsets, attributes, candidates, itemsets_with_support

data = pd.read_csv('h1b_kaggle.csv', na_values = 'NaN')
data = data.drop(columns = ['Unnamed: 0', 'PREVAILING_WAGE', 'YEAR', 'lon', 'lat'])
data = data.dropna()
n_rows = len(data.index)

json_dict = {}




def convert(o):
    if isinstance(o, np.int64): 
    	return int(o)  
    raise TypeError



#print(json_str)


def processData( threshold, length, column):
    if column[0] == '':
        apriori(data, threshold, length)
    else:
        apriori(data, threshold, length, columns=column)
    json_str = json.dumps(json_dict, default=convert)
    return json_str


####################################################### DONE ########################################################

# Implement print pretty
# Identify case status
# Display item support

####################################################### TODOs #######################################################

# Try algorithm on different datasets
# Eliminate highly correlated columns
# Improve time complexity
# Finish documentation
# Add association rule mining
# Divide chunks of code into helper functions
# Develop a better algorithm for finding candidates
# Propose application functions from Apriori results

# Fix bugs: 
#   (FIXED) 1. itemsets do not display properly for thresholds >= 0.02
#   (FIXED) 2. gets 'single positional indexer is out-of-bounds' error for n = len(data.columns)
#   (FIXED) 3. strings with multiple words are split when printing with PrettyPrinter
#           4. dataframe is filtered incorrectly and overlooks attributes
