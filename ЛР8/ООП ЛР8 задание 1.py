class Vector:
    def __init__(self, *args):
        self.values = []
        for n in args:
            if isinstance(n, int):
                self.values.append(n)
    def __str__(self):
        if self.values:
            return f'Вектор {tuple(sorted(self.values))}'
        else:
            return 'Пустой вектор'
v1 = Vector(1, 2, 3)  # создает объект класса v1
print(v1) # выводит "Вектор (1,2,3)"
v2 = Vector()# создает объект класса v2
print(v2)# выводит "пустой вектор "