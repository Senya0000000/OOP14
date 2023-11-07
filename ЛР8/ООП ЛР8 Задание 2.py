class Vector:
    def __init__(self,*args):#конструктор получает произвольное количество аргументов
        self.values = []
        for arg in args:
            if isinstance(arg,int):
                self.values.append(arg)
            self.values.sort()
    def __str__(self):
        if len(self.values) == 0:
            return 'пусть вектор'
        return f'вектор{tuple(self.values)}'
    def __add__(self, other):
        new_v=[]
        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                for i in range(len(self.values)):
                    new_v.append(self.values[i] + other.values[i])
                return Vector(*[i for i in new_v])
            else:
                print('сложение векторов разной длины недопустимо.')            
        if isinstance(other, int):
            for i in range(len(self.values)):
                new_v.append(self.values[i]+other)
            return Vector(*[i for i in new_v])
        if not isinstance(other, (Vector, int)):
                print(f'Вектор нельзя сложить с {other}')
    def __mul__(self, other):
#Умножает два вектора
        new_v=[]
        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                for i in range(len(self.values)):
                    new_v.append(self.values[i] * other.values[i])
                return Vector(*[i for i in new_v])
            else:
                print('сложение векторов разной длины недопустимо.')            
        if isinstance(other, int):
            for i in range(len(self.values)):
                new_v.append(self.values[i]*other)
            return Vector(*[i for i in new_v])
        if not isinstance(other, (Vector, int)):
                print(f'Вектор нельзя сложить с {other}')
# Создаём объекты вектор и выполняем операции
v1=Vector(1,2,3)#создает объект класса v1
print(v1)
v2=Vector(5,9,3,10)
print(v2)    
v3=Vector(7,11,4,15)
print(v3)  
print(v2+v3)# Складываем v2 и v3
print(v2*v3)# Умножаем v2 и v3