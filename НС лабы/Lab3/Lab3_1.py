import requests
import pandas as pd
import math
from sklearn.preprocessing import OneHotEncoder
from decimal import *
import numpy as np


getcontext().prec = 4 # окружгление до 6 знака после запятой

# url = "https://www.dropbox.com/s/bbm6rxqb4bsfl2d/training_data.xlsx?dl=1"
# r = requests.get(url, allow_redirects=True)
# open('training_data.xlsx', 'wb').write(r.content)
#
#
# url = "https://www.dropbox.com/s/gjhur7eyzcv265y/test_data.xlsx?dl=1"
# r = requests.get(url, allow_redirects=True)
# open('test_data.xlsx', 'wb').write(r.content)


training_data = pd.read_excel('D:/Valerian/Documents/OneDrive/Python/ДопОбр Анализ данных/НС лабы/Lab3/training_data.xlsx', usecols=lambda x: 'Unnamed' not in x, na_values=[''], keep_default_na=False)
test_data = pd.read_excel('D:/Valerian/Documents/OneDrive/Python/ДопОбр Анализ данных/НС лабы/Lab3/test_data.xlsx', usecols=lambda x: 'Unnamed' not in x, na_values=[''], keep_default_na=False)
# Заменяем NaN на 'None'
training_data = training_data.fillna("0")
test_data = test_data.fillna("0")



class Perceptron():
  def __init__(self, training_dataset, test_dataset):
    self.training_dataset = training_dataset
    self.test_dataset = test_dataset
    self.train()

  def sigmoid(self,x):
    try:
      #print(f"{x=}")
      sig = (1 / (1 + math.exp(-x)))

      return sig
    except:
      print(f"{x=}")

  # Функция для расчета ошибки (среднеквадратичная ошибка)
  def mse(self, target, pred_score):
    try:
      mean = (target - pred_score)**2
      return mean
    except:
      print(f"{target=} ,{pred_score=}")

  def mae(self, target, pred_score):
    try:
      mean = math.sqrt(self.mse(target, pred_score))
      return mean
    except:
      print(f"{target=} ,{pred_score=}")

  def multiclass_logistic_regression(self,weights, inputs):
    z=0
    #print(f"{z=}, {len(weights)=}, {len(inputs)=}")
    for j in range(len(weights)):
      z += weights[j] * np.float32(inputs[j])
    score = self.sigmoid(z)
    return score

  def update_weights(self,weights, inputs, target, learning_rate):
    new_weights = []
    score1 = self.multiclass_logistic_regression(weights, inputs)
    for i in range(24):
      if target > score1:
        new_weights.append(weights[i] + learning_rate)
      elif target < score1:
        new_weights.append(weights[i] - learning_rate)
      score1 = self.multiclass_logistic_regression(weights, inputs)



    return new_weights

  def train(self):
    num_features = 24 # Количество признаков
    weights = [0.5 for _ in range(num_features)]  # Веса для каждого класса
    learning_rate = 0.001  # Скорость обучения
    num_epochs = 2
    # Количество эпох обучения
    for epoch in range(num_epochs):
      for i in range(len(self.training_dataset)):
        inputs = self.training_dataset[i][1:]
        target = self.training_dataset[i][0]
        weights = self.update_weights(weights, inputs, target, learning_rate)
    self.test_training_dataset(weights)
    self.testing(weights)

  def test_training_dataset(self,weights):
    predictions_mse = 0
    predictions_mae = 0
    for i in range(len(self.training_dataset)):
      inputs = self.training_dataset[i][1:]
      target = self.training_dataset[i][0]
      score = self.multiclass_logistic_regression(weights, inputs)
      predictions_mse += self.mse(target,score)
      predictions_mae += self.mae(target,score)
    MSE = predictions_mse / len(self.training_dataset)
    MAE = predictions_mae / len(self.training_dataset)
    print(f"Точность модели MSE на обучающем датасете: {MSE }")
    print(f"Точность модели MAE на обучающем датасете: {MAE}")

  def testing(self,weights):
    predictions_mse = 0
    predictions_mae = 0
    for i in range(len(self.test_dataset)):
      inputs = self.test_dataset[i][1:]
      target = self.test_dataset[i][0]
      score = self.multiclass_logistic_regression(weights, inputs)
      predictions_mse += self.mse(target, score)
      predictions_mae += self.mae(target, score)
    MSE = predictions_mse / len(self.training_dataset)
    MAE = predictions_mae / len(self.training_dataset)
    print(f"Точность MSE модели  на тестовом датасете: {MSE}")
    print(f"Точность MAE модели  на тестовом датасете: {MAE}")

def encode_text_column(data):
    data_array = data.values
    data_df = pd.DataFrame(data_array)

    text_col_array = data_array[5:9]
    text_col_array= text_col_array.T.tolist()


    # One-hot encoding категориальных данных
    encoder = OneHotEncoder()

    encoded_categorical_data = encoder.fit_transform(text_col_array).toarray()

    data_df = data_df.drop(data_df.columns[[5, 6, 7, 8]], axis=1)
    print(f"{data_df=}")
    print(f"{len(data_df)=}")
    data_df = pd.concat([data_df,pd.DataFrame(encoded_categorical_data)],axis=1)
    data_df = data_df.to_numpy().tolist()

    return data_df

training_data = encode_text_column(training_data)
test_data = encode_text_column(test_data)

perceptron = Perceptron(training_data, test_data)



