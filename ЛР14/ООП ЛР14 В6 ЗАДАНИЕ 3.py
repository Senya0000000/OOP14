from tkinter import *  # Импорт всех компонентов из Tkinter
from tkinter import ttk  # Импорт дополнительных виджетов (тематических)

window = Tk()  # Создание основного окна приложения
window.geometry("300x80")  # Установка размеров окна. Размер увеличен для удобства расположения вертикального прогресс-бара

value_var = IntVar()  # Создание числовой переменной для отслеживания прогресса

# Создание Progressbar и его настройка на горизонтальное  отображение
pb = ttk.Progressbar(window, orient="horizontal", length=280, variable=value_var, mode='determinate')
pb.pack()  # Упаковка прогресс-бара в окно для отображения


# Функция, которая начинает движение прогресс-бара с заданным интервалом
def start():
    pb.start(100)


# Функция, которая останавливает движение прогресс-бара
def stop():
    pb.stop()


# Создание кнопки "Start", которая вызывает функцию start при нажатии
start_btn = ttk.Button(window, text="Start", command=start)
start_btn.pack()  # Упаковка кнопки Start

# Создание кнопки "Stop", которая вызывает функцию stop при нажатии
stop_btn = ttk.Button(window, text="Stop", command=stop)
stop_btn.pack()  # Упаковка кнопки Stop

window.mainloop()  # Запуск основного цикла программы, который ожидает событий (вроде нажатий)