import numpy as np

matrix1 = np.array([[0, 1, 0],
                    [1, 1, 1],
                    [0, 1, 0]])

kernel = np.array([[0, 2, 3],
                   [2, 4, 1],
                   [0, 13, 0]])

result = np.zeros_like(matrix1)  # Создаем матрицу для результата свертки

# Выполняем свертку
for i in range(matrix1.shape[0]):
    for j in range(matrix1.shape[1]):
        result[i, j] = np.sum(matrix1[i:i+kernel.shape[0], j:j+kernel.shape[1]] * kernel)

print("Результат свертки:")
print(result)
