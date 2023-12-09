class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Person: {self.name}, Age: {self.age}, Gender: {self.gender}"

class Student(Person):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self.student_id = student_id

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}, Gender: {self.gender}, Student ID: {self.student_id}"

class Father(Person):
    def __init__(self, name, age, gender, family_members):
        super().__init__(name, age, gender)
        self.family_members = family_members

    def __str__(self):
        return f"Father: {self.name}, Age: {self.age}, Gender: {self.gender}, Family Members: {self.family_members}"

class StudentFather(Student, Father):
    def __init__(self, name, age, gender, student_id, family_members):
        # Явно вызываем конструктор Father
        Father.__init__(self, name, age, gender, family_members)
        # Затем вызываем конструктор Student
        Student.__init__(self, name, age, gender, student_id)

    def __str__(self):
        # Вывод информации о студенте-отце семейства
        return f"Student-Father: {self.name}, Age: {self.age}, Gender: {self.gender}, Student ID: {self.student_id}, Family Members: {self.family_members}"

# Пример использования классов
person1 = Person("John Doe", 30, "Male")
print(person1)

student1 = Student("Alice Smith", 22, "Female", "S12345")
print(student1)

father1 = Father("Bob Johnson", 40, "Male", ["Spouse", "Child1", "Child2"])
print(father1)

student_father1 = StudentFather("Charlie Brown", 35, "Male", "S67890", ["Spouse", "Child1", "Child2"])
print(student_father1)