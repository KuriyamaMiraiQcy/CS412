#!/usr/bin/env python
# coding: utf-8

# In[58]:


import sys

def readFile(filename):
    f = open(filename)
    lines = f.readlines()
    return [x.strip().split(" ") for x in lines]


# In[59]:
"""

training_data = readFile("nursery.train")
testing_data = readFile("nursery.test")


# In[60]:


training_data


# In[61]:


testing_data
"""

# In[62]:


def remove_index(data):
    for i in range(len(data)):
        for j in range(1, len(data[i])):
            data[i][j] = data[i][j].split(":")[1]


# In[63]:

"""
remove_index(training_data)
training_data


In[64]:


remove_index(testing_data)
testing_data
"""

# In[65]:


def dictinct_value(data, column_index):
    value_set = set()
    for row in data:
        value_set.add(row[column_index])
    return list(value_set)


# In[89]:
"""

dictinct_value(training_data, 1)


# In[67]:


dictinct_value(training_data, 2)
"""

# In[68]:


def partition(data, column_index):
    values = dictinct_value(data, column_index)
    partition_data = []
    for i in range(len(values)):
        partition_data.append([])
    for row in data:
        for i in range(len(values)):
            if row[column_index] == values[i]:
                partition_data[i].append(row)
    return partition_data


# In[69]:
"""

partition(training_data, 2)


# In[70]:


training_data
"""

# In[71]:


def count_labels(data):
    count = {}
    for row in data:
        if row[0] not in count:
            count[row[0]] = 1
        else:
            count[row[0]] += 1
    return count


# In[72]:


# count_labels(training_data)


# In[73]:


def calculate_gini(data):
    labels = count_labels(data)
    gini_index = 1
    for key in labels:
        gini_index -= (labels[key] / len(data)) ** 2
    return gini_index


# In[74]:


def gini(data, column_index):
    partition_data = partition(data, column_index)
    if len(partition_data) == 1:
        return 2
    count = 0
    for subset in partition_data:
        count += len(subset) / len(data) * calculate_gini(subset)
    return count


# In[75]:


# gini(training_data, 5)


# In[80]:


def find_best_split(data):
    min_gini = 1
    min_gini_index = 1
    for i in range(1, len(data[0])):
        gini_val = gini(data, i)
        if gini_val < min_gini:
            min_gini = gini_val
            min_gini_index = i
    if min_gini < 1:
        return min_gini_index
    return -1


# In[81]:


# find_best_split(training_data)


# In[84]:


class Decision_Tree:
    def __init__(self, index, children):
        self.index = index
        self.children = children


# In[106]:


class Leaf:
    def __init__(self, data):
        dict = count_labels(data)
        max = 0
        predict = 0
        for x in dict:
            if dict[x] > max:
                max = dict[x]
                predict = x
        self.predict = predict


# In[107]:


def build_decision_tree(data):
    index = find_best_split(data)
    values = dictinct_value(data, index)
    
    if len(count_labels(data)) == 1 or index == -1:
        return Leaf(data)
    
    partition_data = partition(data, index)
    
    children_dict = {}
    for i in range(len(values)):
        child = build_decision_tree(partition_data[i])
        children_dict[values[i]] = child
    return Decision_Tree(index, children_dict)    


# In[108]:


def print_tree(node, spacing=""):
    """World's most elegant tree printing function."""

    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        print (spacing + "Predict:" + str(node.predict))
        return

    # Print the question at this node
    print (spacing + str(node.index))

    for x in node.children:
        print(spacing + x)
        print_tree(node.children[x], spacing+" ")


# In[109]:


# root = build_decision_tree(training_data)


# In[110]:


# print_tree(root)


# In[126]:


def classify(row, root):
    if isinstance(root, Leaf):
        return root.predict
    
    value = row[root.index]
    if value not in root.children:
        min_distance = sys.maxsize
        key_value = 0
        for x in root.children:
            if abs(int(x) - int(value)) < min_distance:
                min_distance = abs(int(x) - int(value))
                key_value = x
        return classify(row, root.children[key_value])
    return classify(row, root.children[value])


# In[127]:


# classify(testing_data[0], root), testing_data[0][0]


# In[137]:


def accuracy(training_data, testing_data):
    right_answer = 0
    root = build_decision_tree(training_data)
    for x in testing_data:
        prediction = classify(x, root)
        if prediction == x[0]:
            right_answer += 1
    print(right_answer / len(testing_data))
    return
"""
accuracy(training_data, testing_data)


# In[138]:


balance_training = readFile("balance.scale.train")
balance_testing = readFile("balance.scale.test")
remove_index(balance_training)
remove_index(balance_testing)
accuracy(balance_training, balance_testing)


# In[139]:


led_training = readFile("led.train")
led_testing = readFile("led.test")
remove_index(led_training)
remove_index(led_testing)
accuracy(led_training, led_testing)


# In[140]:


syn_training = readFile("synthetic.social.train")
syn_testing = readFile("synthetic.social.test")
remove_index(syn_training)
remove_index(syn_testing)
accuracy(syn_training, syn_testing)
"""

# In[141]:


def predictions(root, testing_data):
    prediction_values = []
    for x in testing_data:
        prediction_values.append(classify(x, root))
    return prediction_values


# In[142]:


def decision_tree_model(training_file, testing_file):
    training_data = readFile(training_file)
    testing_data = readFile(training_file)
    remove_index(training_data)
    remove_index(testing_data)
    root = build_decision_tree(training_data)
    return predictions(root, testing_data)


# In[143]:


# decision_tree_model("synthetic.social.train", "synthetic.social.test")


# In[ ]:




