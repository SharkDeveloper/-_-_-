import numpy as np
import pandas as pd
import requests

# url = "https://www.dropbox.com/s/bbm6rxqb4bsfl2d/training_data.xlsx?dl=1"
# r = requests.get(url, allow_redirects=True)
# open('training_data.xlsx', 'wb').write(r.content)
#
#
# url = "https://www.dropbox.com/s/gjhur7eyzcv265y/test_data.xlsx?dl=1"
# r = requests.get(url, allow_redirects=True)
# open('test_data.xlsx', 'wb').write(r.content)


# Чтение данных из файлов Excel
training_data = pd.read_excel('D:/Valerian/Documents/OneDrive/Python/ДопОбр Анализ данных/НС лабы/Lab3/training_data.xlsx',usecols=lambda x: 'Unnamed' not in x, na_values=[''], keep_default_na=False)
test_data     = pd.read_excel('D:/Valerian/Documents/OneDrive/Python/ДопОбр Анализ данных/НС лабы/Lab3/test_data.xlsx',usecols=lambda x: 'Unnamed' not in x, na_values=[''], keep_default_na=False)
# Заменяем NaN на 'None'
training_data = training_data.fillna("0")
test_data = test_data.fillna("0")

# Определение категориальных и числовых признаков
categorical_features = [ 5, 6, 7, 8]
numerical_features = [1, 2, 3, 4, 9,  10, 11,12]

def data_preparation(data):
    # Кодирование категориальных признаков
    def one_hot_encode(data, categorical_features):
        categories = [list(set([row[i] for row in data])) for i in categorical_features]
        encoded_data = []
        for row in data:
            encoded_row = []
            for i, feature in enumerate(row):
                if i in categorical_features:
                    one_hot = [0] * len(categories[categorical_features.index(i)])
                    one_hot[categories[categorical_features.index(i)].index(feature)] = 1
                    encoded_row.extend(one_hot)
                else:
                    encoded_row.append(feature)
            encoded_data.append(encoded_row)
        return np.array(encoded_data)

    encoded_data = one_hot_encode(data, categorical_features)

    # Разделение данных на признаки (X) и целевую переменную (y)
    X = np.array(encoded_data[:, 1:],dtype=float)
    Y = np.array(encoded_data[:, 0],dtype=float)


    # Нормализация числовых признаков
    for feature in numerical_features:
        idx = feature - 2  # сдвиг из-за удаления 'price' в X
        mean = np.mean(X[:, idx].astype(float))
        std = np.std(X[:, idx].astype(float))
        X[:, idx] = (X[:, idx].astype(float) - mean) / std

    # Разделение данных на тренировочную и тестовую выборки
    def train_test_split(X, y, test_size=0.2):
        indices = np.random.permutation(X.shape[0])
        test_size = int(X.shape[0] * test_size)
        test_indices = indices[:test_size]
        train_indices = indices[test_size:]
        return X[train_indices], X[test_indices], y[train_indices], y[test_indices]
    return X,Y

X_train, Y_train = data_preparation(training_data.values.tolist())
X_test, Y_test  = data_preparation(test_data.values.tolist())
# Добавление нового столбца к X_test
# Например, новый столбец с постоянным значением 1
new_column = np.ones((X_test.shape[0], 1))

# Добавление нового столбца к X_test
X_test = np.hstack((X_test, new_column))



# Определение модели нейронной сети
class NeuralNetwork:
    def __init__(self, input_size, hidden_layer_sizes, output_size):
        self.weights = []
        self.biases = []
        layer_sizes = [input_size] + hidden_layer_sizes + [output_size]
        for i in range(len(layer_sizes) - 1):
            self.weights.append(np.random.randn(layer_sizes[i], layer_sizes[i + 1]))
            self.biases.append(np.zeros((1, layer_sizes[i + 1])))

    def relu(self, x):
        return np.maximum(0, x)

    def relu_derivative(self, x):
        return np.where(x > 0, 1, 0)

    def forward(self, X):
        activations = [X]
        for i in range(len(self.weights)):
            z = activations[-1].dot(self.weights[i]) + self.biases[i]
            a = self.relu(z) if i < len(self.weights) - 1 else z  # Linear activation in output layer
            activations.append(a)

        return activations

    def backward(self, activations, y, learning_rate):
        m = y.shape[0]
        deltas = [activations[-1] - y.reshape(-1, 1)]
        for i in range(len(self.weights) - 1, 0, -1):
            deltas.append(deltas[-1].dot(self.weights[i].T) * self.relu_derivative(activations[i]))
        deltas.reverse()
        for i in range(len(self.weights)):
            self.weights[i] -= learning_rate * activations[i].T.dot(deltas[i]) / m
            self.biases[i] -= learning_rate * np.sum(deltas[i], axis=0, keepdims=True) / m

    def train(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            activations = self.forward(X)
            self.backward(activations, y, learning_rate)
            if epoch % 100 == 0:
                loss = np.mean((activations[-1] - y.reshape(-1, 1)) ** 2)
                print(f'Epoch {epoch}, Loss: {loss}')

    def predict(self, X):
        return self.forward(X)[-1]

# Инициализация и обучение модели
input_size = X_train.shape[1]
hidden_layer_sizes = [64, 32]
output_size = 1

nn = NeuralNetwork(input_size, hidden_layer_sizes, output_size)
nn.train(X_train, Y_train, epochs=1000, learning_rate=0.01)

# Оценка модели на тестовых данных
Y_pred = nn.predict(X_test)

mae = np.mean(np.abs(Y_pred - Y_test.reshape(-1, 1)))
mse = np.mean((Y_pred - Y_test.reshape(-1, 1)) ** 2)

print(f'Test MAE: {mae}')
print(f'Test MSE: {mse}')
