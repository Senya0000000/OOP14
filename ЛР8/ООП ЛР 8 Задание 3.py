class Quadrilateral:
    def __init__(self, width, height=None):
        if height is None:
            height = width
        self.width = width
        self.height = height
    def __str__(self):
        if self.width == self.height:
            return f"Куб размером {self.width}х{self.height}"
        else:
            return f"Прямоугольник размером {self.width}х{self.height}"
    def __bool__(self):
        return self.width == self.height
        # Создание объекта Quadrilateral с одним аргументом
quad1 = Quadrilateral(10)
print(quad1)       # Выводит Куб размером 10х10
print(bool(quad1)) # Выводит True
# Создание объекта Quadrilateral с двумя аргументами
quad2 = Quadrilateral(3, 5)
print(quad2)       # Выводит Прямоугольник размером 3х5
print(bool(quad2)) # Выводит False