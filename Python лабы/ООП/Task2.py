"""
    Задача 2: Наследование
    Создайте класс Employee, который наследует от класса Person.
    Добавьте свойство position и метод work, который выводит строку "{name} is working as a {position}."
"""

from Task1 import Person

class Emloyee(Person):
    """
    Представляет сотрудника, который также является человеком(Person).

    Args:
        name (str): Имя человека.
        age (int): Возраст человека.
        position (str): Должность сотрудника.
    """
    def __init__(self,name , age, position: str):
        """
        Инициализирует новый экземпляр класса Employee.

        Args:
            name (str): Имя человека.
            age (int): Возраст человека.
            position (str): Должность сотрудника.
        """
        super().__init__( name , age)
        self.position = position

    def work(self):
        """
        Выводит сообщение, указывающее, что сотрудник работает.
        Example:
            employee = Employee("Боб", 25, "Разработчик")
            employee.work()
            Боб работает в должности Разработчик.
        """
        print(f"{self.name} is working as a {self.position}")

if __name__ == '__main__':
    empoyee = Emloyee("John",18, "Home")
    empoyee.print_info()
    empoyee.work()
