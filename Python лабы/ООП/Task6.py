"""
    Задача 6: Абстракция
    Создайте абстрактный класс Animal с абстрактным методом sound.
    Создайте подклассы Dog и Cat, которые реализуют метод sound
    (собаки лают, кошки мяукают).
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """
    ABC для различных животных
    """
    @abstractmethod
    def sound(self):
        """
        Воспроизведения звуков животных. Подклассы должны реализовать этот метод
        """
        pass

class Dog(Animal):
    """
    Представление собаки
    """
    def sound(self):
        """
        Воспроизведение звуков собаки
        """
        print("Gaw gaw")

class Cat(Animal):
    """
    Представление кота
    """
    def sound(self):
        """
        Воспроизведение звуков кошики
        """
        print("meow")

if __name__ == "__main__":
    animals = [Dog(), Cat(), Animal()]
    for animal in animals:
        animal.sound()