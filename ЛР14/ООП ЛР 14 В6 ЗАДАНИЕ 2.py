from tkinter import *  # Импортируем все из модуля tkinter

window = Tk()  # Создаем основное окно приложения
window.geometry("250x200")  # Устанавливаем размер окна 250x200 пикселей

# Создаем первый виджет Listbox. Параметр height задает количество отображаемых строк, width — ширину,
# selectmode EXTENDED позволяет выбирать несколько элементов списка
list1 = Listbox(window, height=5, width=15, selectmode=EXTENDED)

# Создаем второй виджет Listbox. Здесь selectmode SINGLE означает, что можно выбрать только один элемент списка
list2 = Listbox(window, height=5, width=15, selectmode=SINGLE)

# Задаем содержимое первого списка
lst1 = ['Минск', 'Молодечно', 'Борисов', 'Жодино', 'Воложин']
# Задаем содержимое второго списка
lst2 = ['Гродно', 'Ивье', 'Новогрудок', 'Ошмяны', 'Островец']

# Добавляем содержимое lst1 в первый Listbox
for i in lst1:
    list1.insert(END, i)

# Добавляем содержимое lst2 во второй Listbox
for i in lst2:
    list2.insert(END, i)

# Упаковываем первый Listbox с помощью менеджера геометрии pack, который разместит его в окне
list1.pack()
# Аналогично упаковываем второй Listbox
list2.pack()

# Запускаем цикл обработки событий окна
window.mainloop()