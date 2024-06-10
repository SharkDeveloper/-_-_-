import random
import math

dataset = list()

actions = ['+','-', "/", "*"]


for i in range(1000):
  temp = list()
  temp.append(random.randint(-100, 100) * 0.01)
  temp.append(random.randint(-100, 100) * 0.01)
  temp.append(random.randint(0, 3))
  if temp[2] == 1:
    if temp[0] - temp[1] < 0:
      temp.append(0)
    elif temp[0] - temp[1] == 0:
      temp.append(1)
    else:
      temp.append(2)
  elif temp[2] == 0:
    if temp[0] + temp[1] < 0:
      temp.append(0)
    elif temp[0] + temp[1] == 0:
      temp.append(1)
    else:
      temp.append(2)
  elif temp[2] == 2:
    if temp[1] == 0:
      temp.append(3)
    elif temp[0] / temp[1] < 0:
      temp.append(0)
    elif temp[0] / temp[1] == 0:
      temp.append(1)
    else:
      temp.append(2)
  elif temp[2] == 3:
    if temp[0] * temp[1] < 0:
      temp.append(0)
    elif temp[0] * temp[1] > 0:
      temp.append(2)
    else:
      temp.append(1)

  dataset.append(temp)


class Perceptron():
  def __init__(self, training_dataset, test_dataset):
    self.training_dataset = training_dataset
    self.test_dataset = test_dataset
    self.train()

  def sigmoid(self,x):
    sig = (1 / (1 + math.exp(-x)))
    return sig

  def multiclass_logistic_regression(self,weights, inputs):
    scores = []
    for i in range(4):  # Четыре класса
      z = weights[i][0]  # Смещение (bias) для i-го класса
      for j in range(len(weights[i]) - 1):

        z += weights[i][j + 1] * inputs[j]
      scores.append(self.sigmoid(z))
    return scores

  def update_weights(self,weights, inputs, target, learning_rate):
    new_weights = []
    scores = self.multiclass_logistic_regression(weights, inputs)
    for i in range(4):  # Четыре класса
      error = 1 if i == target else 0  # Целевой класс
      error -= scores[i]  # Градиент

      new_weights.append([weights[i][0] + learning_rate * error])
      for j in range(len(weights[i]) - 1):
        new_weights[i].append(weights[i][j + 1] + learning_rate * error * inputs[j])
    return new_weights

  def train(self):
    num_features = 3 # Количество признаков
    weights = [[0.05 for _ in range(num_features)] for _ in range(4)]  # Веса для каждого класса
    learning_rate = 0.00001  # Скорость обучения
    num_epochs = 1000  # Количество эпох обучения
    for epoch in range(num_epochs):
      for i in range(len(self.training_dataset)):
        inputs = self.training_dataset[i][:3]
        target = self.training_dataset[i][3]
        weights = self.update_weights(weights, inputs, target, learning_rate)
    self.test_training_dataset(weights)
    self.test(weights)

  def test_training_dataset(self,weights):
    correct_predictions = 0
    for i in range(len(self.training_dataset)):
      inputs = self.training_dataset[i][:3]
      target = self.training_dataset[i][3]
      scores = self.multiclass_logistic_regression(weights, inputs)
      predicted_class = scores.index(max(scores))
      if predicted_class == target:
        correct_predictions += 1

    accuracy = correct_predictions / len(self.training_dataset)
    print(f"Точность модели на обучающем датасете: {accuracy * 100}%")

  def test(self,weights):
    correct_predictions = 0
    for i in range(len(self.test_dataset)):
      inputs = self.test_dataset[i][:3]
      target = self.test_dataset[i][3]
      scores = self.multiclass_logistic_regression(weights, inputs)
      predicted_class = scores.index(max(scores))
      if predicted_class == target:
        correct_predictions += 1

    accuracy = correct_predictions / len(self.test_dataset)
    print(f"Точность модели на тестовом датасете: {accuracy * 100}%")



perceptron = Perceptron(dataset[:800],dataset[800:])
