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

        
def apriori_1(data, support):
    """ 
    First iteration of Apriori.
  
    Parameters: 
    data (pandas dataframe): Description of arg1 
    support (int):

    Returns: 
    data:
    itemsets:
    attributes:
    """
    
    itemsets = {}
    for i in range(len(data.columns)):
        column = data.iloc[:, i]
        values = column.unique()
        frequent = column.value_counts()[column.value_counts() / n_rows > support]
        indices = list(frequent.index)
        values = list(frequent.values)
        items = dict(zip(indices, values))
        name = frequent.name
        itemsets[name] = items
        
    attributes = {}
    for key, value in itemsets.items():
        attributes[key] = set(value)
        
    ## Filters dataframe to eliminate infrequent values
    for key, value in attributes.items():
        data = data[data[key].isin(value)]

    return data, itemsets, attributes


def apriori_n(data, attribute_list, support, n):
    """ 
    Nth iteration of Apriori.
  
    Parameters: 
    data (pandas dataframe): Description of arg1
    attribute_list:
    support (int):
    n (int):

    Returns: 
    data:
    itemsets:
    attributes:
    """
      
    
    ## Constructs collection of frequent itemsets
    ## itemsets: key - index tuple, value - list of frequent itemsets tuple
    itemsets = {}
    for item in list(itertools.combinations(attribute_list.keys(), n)): # Makes a combination of n attributes
        frequent = []
        grouped = data.groupby(list(item)).count().iloc[:,0] / n_rows > support # Groups data by attribute and filters only itemsets occuring above threshold
        for index in grouped[grouped[grouped.index] == True].index: # Extracts frequent indices
            frequent.append(index)
        itemsets[item] = frequent
    
    
    ## Constructs collection of frequent itemsets with support
    ## itemsets_with_support: key - index tuple, value - dictionary of frequent itemsets with attribute as key and count as value
    itemsets_with_support = {}
    for item in list(itertools.combinations(attribute_list.keys(), n)): # Makes a combination of n attributes
        frequent = data.groupby(list(item)).count().iloc[:,0] # Groups data by attribute
        frequent = frequent[frequent / n_rows > support] # Filters only itemsets occuring above threshold
        indices = list(frequent.index)
        values = list(frequent.values)
        items = dict(zip(indices, values)) # Constructs dictionary with attribute as key and count as value
        itemsets_with_support[item] = items 
        
        
    ## Constructs collection of frequent attributes
    ## attributes: key - column name, value - set of frequent attributes
    attributes = {}
    for key, arr in itemsets.items(): 
        for k in key:
            if k not in attributes:
                attributes[k] = set([]) # Builds a set for each column name
        for k in key:
            for value in arr:
                for i in range(len(value)):
                    attributes[key[i]].add(value[i]) # Adds freqent attributes to sets
    
    
    ## Constructs collection of combinations of frequent attributes
    ## reverse: set of multi-indices
    reverse = set()
    for key, value in itemsets.items():
        for item in value:
            reverse.add(item)
    
    
    ## Filters dataframe to eliminate infrequent values
    for key, value in attributes.items():
        data = data[data[key].isin(value)]
        
        
    return data, itemsets, attributes, itemsets_with_support

data = pd.read_csv('hotel_cleaned.csv')
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
