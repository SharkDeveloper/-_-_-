"""
    Задача 5: Композиция
    Создайте класс Engine с методом start, который выводит строку "Engine started."
    Создайте класс Car, который имеет объект Engine и метод drive,
    который вызывает метод start объекта Engine и выводит строку "Car is driving."
"""

class Engine:
    """
    Представляет двигатель автомобиля.
    """
    def start(self):
        """
        Запускает двигатель.
        """
        print("Engine started")

class Car:
    """
    Представляет автомобиль
    """

    def __init__(self, engine: Engine):
        """
        Иницилизирует автомобиль(Cat).
        Args:
            engine(Engine): Двигатель автомобиля:
        """
        self.engine = engine

    def drive(self):
        """
        Запускает двигатель и приводит автомобиль в движение.
        """
        self.engine.start()
        print("Car is driving")

if __name__ == "__main__":
    engine = Engine()
    car = Car(engine)
    car.drive()