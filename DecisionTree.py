import sys
from collections import deque

gini_dict = {}

def readFile(filename):
    f = open(filename)
    lines = f.readlines()
    return [x.strip().split(" ") for x in lines]

def training(training_data):
    line_number = len(training_data)
    dict_num = len(training_data[0]) - 1
    dict_list = [dict() for x in range(dict_num)]
    training_data = handle_training_data(training_data)

    for line in training_data:
        for i in range(1, len(line)):
            if line[i][1] in dict_list[i - 1]:
                dict_list[i - 1][line[i][1]] += 1
            else:
                dict_list[i - 1][line[i][1]] = 1

    gini_index_array = gini_index(dict_list, line_number)
    gini_index_array = sorted(gini_index_array, reverse=True)
    root = build_decision_tree(gini_index_array, dict_list)
    label_training(root, training_data)

def label_training(root, training_data):


def build_decision_tree(gini_index_array, dict_list):
    global gini_dict
    root = Decision()
    previous = [root]

    for i in range(len(gini_index_array)):
        current = []
        current_keys = dict_list[gini_dict[gini_index_array[i]]].keys()
        for parent in previous:
            children = []
            for x in current_keys:
                node = Decision(x, False, [], [], parent.level + 1)
                children.append(node)
                current.append(node)
            parent.children = children
        previous = current

    for node in previous:
        node.isleaf = True
    return root






def gini_index(dicts, line_number):
    gini_array = []
    global gini_dict
    index = 0

    for dict in dicts:
        count = 0

        for key in dict:
            count += pow(dict[key] / line_number ,2)
        gini_array.append(1 - count)
        gini_dict[1 - count] = index
        index += 1
    return gini_dict

def handle_training_data(training_data):
    for i in range(len(training_data)):
        training_data[i] = [x.split(":") for x in training_data[i]]
    return training_data

class Decision:
    def __init__(self, index="", isleaf=False, label="", children=[], level=-1):
        self.index = index
        self.isleaf = isleaf
        self.label = label
        self.children = children
        self.level = level



