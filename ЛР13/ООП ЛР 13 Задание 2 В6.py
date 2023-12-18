import random
import tkinter as tk

def generate_array():
    size = int(entry.get())
    array = [random.randint(1, 100) for _ in range(size)]
    label_array.config(text="Массив: " + str(array))

def calculate_min():
    array = [int(x) for x in label_array.cget("text").split()[1][1:-1].split(",")]
    min_element = min(array)
    label_result.config(text="Минимальный элемент: " + str(min_element))

def calculate_max():
    array = [int(x) for x in label_array.cget("text").split()[1][1:-1].split(",")]
    max_element = max(array)
    label_result.config(text="Максимальный элемент: " + str(max_element))

def calculate_sum():
    array = [int(x) for x in label_array.cget("text").split()[1][1:-1].split(",")]
    sum_elements = sum(array)
    label_result.config(text="Сумма элементов: " + str(sum_elements))

window = tk.Tk()
window.title("Оконное приложение для работы с массивом")

label_instruction = tk.Label(window, text="Введите размер массива:")
label_instruction.pack()

entry = tk.Entry(window)
entry.pack()

button_generate = tk.Button(window, text="Сгенерировать массив", command=generate_array)
button_generate.pack()

label_array = tk.Label(window, text="Массив: ")
label_array.pack()

frame_buttons = tk.Frame(window)
button_min = tk.Button(frame_buttons, text="Минимальный элемент", command=calculate_min)
button_min.pack(side=tk.LEFT)
button_max = tk.Button(frame_buttons, text="Максимальный элемент", command=calculate_max)
button_max.pack(side=tk.LEFT)
button_sum = tk.Button(frame_buttons, text="Сумма элементов", command=calculate_sum)
button_sum.pack(side=tk.LEFT)
frame_buttons.pack()

label_result = tk.Label(window, text="")
label_result.pack()

window.mainloop()