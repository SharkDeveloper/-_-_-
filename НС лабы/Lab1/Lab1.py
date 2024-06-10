import copy
import random
import numpy as np


class Perceptron:
  def __init__(self,epochs):
    self.weights = np.ones((2,1))
    self.epochs = epochs

  def creat_dataset(self):
    dataset = list()

    dataset.append(([0, 0], 0))
    dataset.append(([0, 1], 1))
    dataset.append(([1, 0], 1))
    dataset.append(([1, 1], 0))

    noise_dataset = list()
    for i in range(10000):
      noise_dataset.append(copy.deepcopy(random.choice(dataset)))
      for j in range(2):
        noise_dataset[i][0][j] += (random.randint(-45, 45) * 0.01)

    return noise_dataset

  def bin_classification(self,input_ind):
    ind = []
    if input_ind[0]-0.5 > 0:
      ind.append(1)
    else:
      ind.append(0)
    if input_ind[1]-0.5 > 0:
      ind.append(1)
    else:
      ind.append(0)
    return ind
  def summator(self,input_ind):
    summator = 0
    for i in range(2):
      summator += input_ind[i]*self.weights[i]
    if summator >0.5 and summator < 1.5:
      return True
    else:
      return False

  def learn(self):
    dataset = self.creat_dataset()
    for i in range(len(dataset)):
      if bool(dataset[i][1]) != self.summator(self.bin_classification(dataset[i][0])):
        self.weights[0][i] = self.weights[0][i]+0.1


  def train(self):
    for i in range(self.epochs):
      self.learn()

  def test(self,input_dataset,test_res):
    res = 0
    for i in range(len(input_dataset)):
      print(f"Входные данные {input_dataset[i]}    Предсказание: {self.summator(self.bin_classification(input_dataset[i]))}")
      if self.summator(self.bin_classification(input_dataset[i])) == test_res[i]:
        res+=1
    print(self.weights)
    print("Accurancy: ",res/len(test_res))

p = Perceptron(10)
p.train()

test_data = list()
test_res = list()
dataset = list()
dataset.append(([0, 0],0))
dataset.append(([0, 1],1))
dataset.append(([1, 0],1))
dataset.append(([1, 1],0))
noise_dataset = list()
for i in range(5000):
  noise_dataset.append(copy.deepcopy(random.choice(dataset)))
  for j in range(2):
    noise_dataset[i][0][j] += (random.randint(-45, 45) * 0.01)
for ind in range(len(noise_dataset)):
  test_data.append(noise_dataset[ind][0])
  test_res.append(noise_dataset[ind][1])
p.test(test_data,test_res)
