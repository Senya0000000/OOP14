from tkinter import *  # Импорт всех компонентов из модуля tkinter
from tkinter import ttk  # Импорт ttk для использования тематических виджетов tk

# Функция для записи информации в файл
def getInfo():
    with open('output.txt', 'w') as file:  # Открытие файла output.txt для записи
        # Запись имени пользователя в файл
        file.write('Имя: ' + nameT.get() + '\n')
        # Запись фамилии пользователя в файл
        file.write('Фамилия: ' + lastNameT.get() + '\n')
        # Проверка и запись пола пользователя
        if polvar.get() == 'm':
            file.write('Пол: мужской\n')
        elif polvar.get() == 'w':
            file.write('Пол: женский\n')
        else:
            file.write('Пол не указан\n')
        # Запись выбранных пользователем предметов
        file.write('Любимые предметы:\n')
        if var1.get() == 1:
            file.write(' - математика\n')
        if var2.get() == 1:
            file.write(' - английский язык\n')
        if var3.get() == 1:
            file.write(' - информационные технологии\n')

# Создание главного окна приложения
window = Tk()
window.title('Регистрация')  # Задание заголовка окна

# Создание и настройка виджетов с метками для имени, фамилии, пола и предметов
name = Label(window, text='Имя', width=20, height=1, fg='blue', font='arial 18')
lastName = Label(window, text='Фамилия', width=20, height=1, fg='blue', font='arial 18')
pol = Label(window, text='Пол', width=20, height=1, fg='blue', font='arial 18')
likePr = Label(window, text='Любимые предметы', width=20, height=1, fg='blue', font='arial 18')

# Создание полей для ввода имени и фамилии
nameT = Entry(window, width=30, font='arial 14')
lastNameT = Entry(window, width=30, font='arial 14')

# Переменная и радиокнопки для выбора пола
polvar = StringVar()
polvar.set(' ')  # Установка начального значения переменной пола
radio1 = Radiobutton(window, text='мужской', variable=polvar, value='m')
radio2 = Radiobutton(window, text='женский', variable=polvar, value='w')

# Переменные и флажки для выбора предметов
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
check1 = Checkbutton(window, text='математика', variable=var1, onvalue=1, offvalue=0)
check2 = Checkbutton(window, text='английский язык', variable=var2, onvalue=1, offvalue=0)
check3 = Checkbutton(window, text='информационные технологии', variable=var3, onvalue=1, offvalue=0)

# Создание и настройка кнопки для отправки формы
btn = Button(window, text='Принять', width=25, height=5, fg='blue', font='arial 14', command=getInfo)

# Расположение виджетов в окне приложения
name.pack()
nameT.pack()
lastName.pack()
lastNameT.pack()
pol.pack()
radio1.pack()
radio2.pack()
likePr.pack()
check1.pack()
check2.pack()
check3.pack()
btn.pack()

# Запуск основного цикла обработки событий окна
window.mainloop()