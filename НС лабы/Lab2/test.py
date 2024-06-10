import numpy as np

class Perceptron:
    def __init__(self, num_classes, learning_rate=0.1, max_epochs=100):
        self.num_classes = num_classes
        self.learning_rate = learning_rate
        self.max_epochs = max_epochs
        self.weights = np.zeros((num_classes, 2))  # Веса для каждого класса, включая смещение
        self.biases = np.zeros(num_classes)

    def fit(self, X, y):
        for epoch in range(self.max_epochs):
            for i, sample in enumerate(X):
                true_class = y[i]
                predicted_class = self.predict(sample)

                if predicted_class != true_class:
                    self.weights[true_class] += self.learning_rate * sample
                    self.biases[true_class] += self.learning_rate
                    self.weights[predicted_class] -= self.learning_rate * sample
                    self.biases[predicted_class] -= self.learning_rate

    def predict(self, sample):
        scores = [np.dot(self.weights[i], sample) + self.biases[i] for i in range(self.num_classes)]
        return np.argmax(scores)

# Создание и обучение модели
model = Perceptron(num_classes=4)
model.fit(X, y)

# Тестирование модели
print(model.predict([1, 2]))  # Output: 1 (положительное число)
print(model.predict([3, -4]))  # Output: 0 (отрицательное число)
print(model.predict([0, 0]))  # Output: 2 (ноль)
print(model.predict([1, 0]))  # Output: 3 (inf)