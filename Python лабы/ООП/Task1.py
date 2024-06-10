"""
    Задача 1: Создание и использование классов
    Создайте класс Person, который имеет свойства name, age и метод introduce,
    который выводит строку "Hello, my name is {name} and I am {age} years old."
"""

class Person:
    """
    Представляет человека с именем и возрастом.
    Args:
        name(str): Имя человека.
        age(int): Возраст человека.
    """
    def __init__(self, name: str , age: int):
        """
        Иницилизирует новый экземпляр класса Person
        Args:
            name(str): Имя человека.
            age(int): Возраст человека.
        """
        self.name = name
        self.age = age

    def print_info(self):
        """
        Печатает приветствие, включающее имя и возраст человека.

        Example:
            person = Person("Алиса", 30)
            person.introduce()
            Привет, меня зовут Алиса и мне 30 лет.
        """
        print(f"Hell, my name is {self.name} and I am {self.age} years old.")

if __name__ == '__main__':
    person = Person("John",10)
    person.print_info()

