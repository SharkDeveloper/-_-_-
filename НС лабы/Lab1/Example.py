import numpy as np
import random
import copy

numbers = list()
numbers.append(([[1, 1, 1],
                 [1, 0, 1],
                 [1, 0, 1],
                 [1, 0, 1],
                 [1, 1, 1]], 0))
numbers.append(([[0, 0, 1],
                 [0, 0, 1],
                 [0, 0, 1],
                 [0, 0, 1],
                 [0, 0, 1]], 1))

numbers.append(([[1, 1, 1],
                 [0, 0, 1],
                 [1, 1, 1],
                 [1, 0, 0],
                 [1, 1, 1]], 2))

numbers.append(([[1, 1, 1],
                 [0, 0, 1],
                 [1, 1, 1],
                 [0, 0, 1],
                 [1, 1, 1]], 3))

numbers.append(([[1, 0, 1],
                 [1, 0, 1],
                 [1, 1, 1],
                 [0, 0, 1],
                 [0, 0, 1]], 4))

numbers.append(([[1, 1, 1],
                 [1, 0, 0],
                 [1, 1, 1],
                 [0, 0, 1],
                 [1, 1, 1]], 5))

numbers.append(([[1, 1, 1],
                 [1, 0, 0],
                 [1, 1, 1],
                 [1, 0, 1],
                 [1, 1, 1]], 6))

numbers.append(([[1, 1, 1],
                 [0, 0, 1],
                 [0, 0, 1],
                 [0, 0, 1],
                 [0, 0, 1]], 7))

numbers.append(([[1, 1, 1],
                 [1, 0, 1],
                 [1, 1, 1],
                 [1, 0, 1],
                 [1, 1, 1]], 8))

numbers.append(([[1, 1, 1],
                 [1, 0, 1],
                 [1, 1, 1],
                 [0, 0, 1],
                 [1, 1, 1]], 9))

"""dataset = list()
for i in range(10000):
  dataset.append(random.choice(numbers))"""

dataset = list()
for i in range(10000):
  dataset.append(copy.deepcopy(random.choice(numbers)))
  for j in range(15):
    dataset[i][0][j//3][j%3] += (random.randint(-50, 50) * 0.01)

first_layer_weights = np.ones((15, 1))

def result_bin_class(result):
    if (result > 8):
        return True
    else:
        return False


def calculate_res(input_number, first_layer_weights):
    sum = 0
    for i in range(15):
        sum += input_number[0][i//3][i%3] * first_layer_weights[i]
    return sum

def weight_changing(positive, target):
    k = 0
    if (positive and not target):
        k = -0.1
    elif (not positive and target):
        k = 0.1
    return k

def learn(input_number, first_layer_weights, target):
    k = weight_changing(result_bin_class(calculate_res(input_number, first_layer_weights)), True if input_number[1] == target else False)
    for i in range(15):
        first_layer_weights[i] += input_number[0][i//3][i%3] * k
    return first_layer_weights

def train_nn(input_dataset, first_layer_weights, target, size_of_data):
    for i in range(size_of_data):
        first_layer_weights = learn(random.choice(input_dataset), first_layer_weights, target)



def tst(input_number, first_layer_weights, target):

    if (result_bin_class(calculate_res(input_number, first_layer_weights)) == (True if input_number[1] == target else False)):
        return 1
    else:
        return 0

def tst_nn( dataset, first_layer_weights, target, size_of_data):
    res = 0
    for i in range(size_of_data):
        res += tst(random.choice(dataset), first_layer_weights, target)
    return (res / size_of_data)

train_nn(dataset, first_layer_weights, 1, 2000)
print(first_layer_weights)
train_nn(dataset, first_layer_weights, 1, 2000)
print(first_layer_weights)
print('Accuracy-score: ', tst_nn(dataset, first_layer_weights, 1, 200))