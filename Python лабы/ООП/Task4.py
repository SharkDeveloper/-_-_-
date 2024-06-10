"""
    Задача 4: Полиморфизм
    Создайте базовый класс Shape с методом area. Создайте два подкласса Rectangle и Circle,
    которые переопределяют метод area для вычисления площади прямоугольника и круга соответственно.
"""

class Shape:
    """
    Абстарктный класс для различных форм
    """
    def area(self):
        """
        Подсчитывет площадь формы. Подкласс должен реализовать метод.
        Raises:
            NotImplementedError: Если метод не реализован подклассом.
        """
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    """
    Представляет прямоугольник.

    Args:
        width (float): Ширина прямоугольника.
        height (float): Высота прямоугольника.
    """
    def __init__(self,width,height):
        """
        Инициализирует новый экземпляр класса Rectangle.

        Args:
            width (float): Ширина прямоугольника.
            height (float): Высота прямоугольника.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Вычисляет площадь прямоугольника.
        """
        print(f"Area Rectangle: {self.width * self.height}")

class Circle(Shape):
    """
    Представляет круг.

    Args:
        radius (float): Радиус круга.
    """
    def __init__(self, radius):
        """
        Инициализирует новый экземпляр класса Circle.

        Args:
            radius (float): Радиус круга.
        """
        self.radius = radius

    def area(self):
        """
        Вычисляет площадь круга.
        """
        print(f"Area Circle: {3.14*self.radius**2}")

if __name__ == '__main__':
    shapes = [Rectangle(10,5), Circle(10), Shape()]
    for shape in shapes:
        shape.area()