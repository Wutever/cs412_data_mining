import pandas as pd
import itertools
import pprint
pp = pprint.PrettyPrinter(width = 200)
import json

def apriori(data, threshold, length):

    if length > len(data.columns)+1:
        raise ValueError('Desired length of itemsets must be smaller or equal to number of attributes.')

    data, itemsets, attributes, candidates = apriori_1(data, threshold)
    json_dict[1] = itemsets
    for n in range(2, length):
        data, itemsets, attributes, candidates = apriori_n(data, itemsets, attributes, candidates, threshold, n)
        #print('length-' + str(n) + ' itemsets:')
        #print(' ')
        #pp.pprint(itemsets)
        #print(' ')
        #print(' ')
        temp_dict = {}
        for key, value in itemsets.items():
            temp_dict[str(key)] = value
        json_dict[n] = temp_dict
    return data, itemsets, attributes, candidates


def apriori_1(data, threshold):

    itemsets = {}
    for i in range(len(data.columns)):
        column = data.iloc[:, i]
        values = column.unique()
        frequent = column.value_counts()[column.value_counts() / n_rows > threshold]
        items = list(frequent.index)
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

    return data, itemsets, attributes, candidates


data = pd.read_csv('h1b_kaggle.csv', na_values = 'NaN')
data = data.drop(columns = ['Unnamed: 0', 'PREVAILING_WAGE', 'YEAR', 'lon', 'lat'])
data = data.dropna()
n_rows = len(data.index)
json_dict = {}
apriori(data, 0.001, 6)
col1 = "frequent pair1"
col2 = "frequent pair2"
frequent = 1


#json_str = json.dumps(list(json_dict.values()))

def processData():

    #s = pprint.pformat(json_dict)
    return(json_dict)

####################################################### TODOs #######################################################

# Display item support
# Implement print pretty
# Try algorithm on different datasets
# Eliminate highly correlated columns
# Improve time complexity
# Finish documentation
# Add association rule mining
# Divide chunks of code into helper functions
# Develop a better algorithm for finding candidates
# Propose application functions from Apriori results
# Link results back to spreadsheet

# Fix bugs: 
#   (FIXED) 1. itemsets do not display properly for thresholds >= 0.02
#   (FIXED) 2. gets 'single positional indexer is out-of-bounds' error for n = len(data.columns)
#   (FIXED) 3. strings with multiple words are split when printing with PrettyPrinter
