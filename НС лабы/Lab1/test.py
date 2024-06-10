import random

class Perceptron:
    def __init__(self, num_inputs):
        # Инициализация весов случайными значениями
        self.weights = [random.random() for _ in range(num_inputs)]
        self.bias = random.random()

    def activation(self, x):
        # Функция активации (пороговая)
        return 1 if x > 0 else 0

    def predict(self, inputs):
        # Расчет выхода нейрона
        total = sum(w * x for w, x in zip(self.weights, inputs)) + self.bias
        return self.activation(total)

    def train(self, training_data, epochs, learning_rate):
        for _ in range(epochs):
            for inputs, target in training_data:
                prediction = self.predict(inputs)
                error = target - prediction
                # Обновление весов в соответствии с правилом перцептрона
                self.weights = [w + learning_rate * error * x for w, x in zip(self.weights, inputs)]
                self.bias += learning_rate * error

# Создание перцептрона
perceptron = Perceptron(num_inputs=2)

# Обучающие данные для функции "ИЛИ"
training_data = [
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 0)
]

# Обучение перцептрона
perceptron.train(training_data, epochs=100, learning_rate=0.1)

# Проверка работы перцептрона
test_data = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

print("Результаты предсказания:")
for inputs in test_data:
    prediction = perceptron.predict(inputs)
    print(f"Входные данные: {inputs}, Предсказание: {prediction}")